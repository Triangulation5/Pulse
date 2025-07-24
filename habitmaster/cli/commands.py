import csv
import json
import shutil
from datetime import datetime, date, timedelta
from pathlib import Path

from db import database
from models.habit import Habit
from rich.console import Console
from utils import heatmap

console = Console()

def add_habit(name, category, description):
    Habit.add(name, category, description)

def delete_habit(name):
    Habit.delete(name)

def rename_habit(old_name, new_name):
    Habit.rename(old_name, new_name)

def list_habits(args):
    Habit.list_all(args.archived)

def log_status(name, date_str, status):
    if date_str == 'today':
        date_str = date.today().isoformat()
    Habit.log(name, date_str, status)

def show_heatmap(names, start=None, end=None):
    if start:
        try:
            start_date = datetime.strptime(start, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Start date must be YYYY-MM-DD format.")
    else:
        start_date = None
    if end:
        try:
            end_date = datetime.strptime(end, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("End date must be YYYY-MM-DD format.")
    else:
        end_date = None
    habits_data = {}
    for name in names:
        logs = Habit.get_logs(name, start=start, end=end)
        habits_data[name] = logs
    heatmap.build_heatmap(habits_data, start_date, end_date)

def set_reminder(name, remind):
    Habit.set_reminder(name, remind)

def archive_habit(name):
    Habit.archive(name)

def unarchive_habit(name):
    Habit.unarchive(name)

def weekly_view(args):
    today = date.today()
    week_ago = today - timedelta(days=6)
    habits = database.list_habits()
    if not habits:
        console.print("No active habits found.", style="yellow")
        return
    
    for habit in habits:
        logs = Habit.get_logs(habit['name'], start=week_ago.isoformat(), end=today.isoformat())
        completions = [d for d, s in logs.items() if s == 'completed']
        console.print(f"[cyan]{habit['name']}[/cyan]: {len(completions)} completions in the last 7 days.")

def monthly_view(args):
    today = date.today()
    month_start = today.replace(day=1)
    habits = database.list_habits()
    if not habits:
        console.print("No active habits found.", style="yellow")
        return

    for habit in habits:
        logs = Habit.get_logs(habit['name'], start=month_start.isoformat(), end=today.isoformat())
        completions = [d for d, s in logs.items() if s == 'completed']
        console.print(f"[cyan]{habit['name']}[/cyan]: {len(completions)} completions this month.")

def import_data(name, fmt, file_path):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File '{file_path}' not found.")
    entries = []
    if fmt == "csv":
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "date" in row and "status" in row:
                    entries.append({"date": row["date"], "status": row["status"]})
    elif fmt == "json":
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                for entry in data:
                    if "date" in entry and "status" in entry:
                        entries.append(
                            {"date": entry["date"], "status": entry["status"]}
                        )
            else:
                raise ValueError(
                    "JSON must contain a list of objects with 'date' and 'status'"
                )
    else:
        raise ValueError("Unsupported import format")
    database.import_logs(name, entries)
    console.print(
        f"Imported habit data for '{name}' from '{file_path}'.", style="green"
    )

def export_data(name, fmt, out_path):
    data = database.export_logs(name)
    path = Path(out_path)
    if fmt == "csv":
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["date", "status"])
            writer.writeheader()
            writer.writerows(data)
    elif fmt == "json":
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    else:
        raise ValueError("Unsupported export format")
    console.print(f"Habit data exported to '{out_path}'.", style="green")

def backup_database(out_path):
    src = database.DB_PATH
    dst = Path(out_path)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    console.print(f"Database backed up to '{out_path}'.", style="green")


def restore_database(file_path):
    src = Path(file_path)
    if not src.exists():
        raise FileNotFoundError(f"Backup file '{file_path}' not found.")
    dst = database.DB_PATH
    shutil.copy2(src, dst)
    console.print(f"Database restored from '{file_path}'.", style="green")
