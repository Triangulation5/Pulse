"""
Root of all the commands. Used in command.py.
"""

from datetime import date, datetime, timedelta

from db import database
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class Habit:
    """Represents a habit."""

    def __init__(
        self, name, category=None, description=None, remind=False, archived=False
    ):
        """Initializes a Habit object."""
        self.name = name
        self.category = category
        self.description = description
        self.remind = remind
        self.archived = archived

    @staticmethod
    def add(name, category=None, description=None):
        """Adds a new habit."""
        if not name or not name.strip():
            raise ValueError("Habit name cannot be empty.")
        database.add_habit(name.strip(), category, description)
        console.print(Panel(f"Habit '{name}' added.", style="green"))

    @staticmethod
    def delete(name):
        """Deletes a habit."""
        database.delete_habit(name)
        console.print(Panel(f"Habit '{name}' deleted.", style="red"))

    @staticmethod
    def rename(old_name, new_name):
        """Renames a habit."""
        if not new_name or not new_name.strip():
            raise ValueError("New habit name cannot be empty.")
        database.rename_habit(old_name, new_name.strip())
        console.print(
            Panel(f"Habit renamed from '{old_name}' to '{new_name}'.", style="yellow")
        )

    @staticmethod
    def list_all(include_archived=False):
        """Lists all habits."""
        habits = database.list_habits(include_archived)
        if not habits:
            console.print(Panel("No habits found.", style="red"))
            return

        table = Table(title="Habits List:")
        table.add_column("Name", style="cyan")
        table.add_column("Category", style="blue")
        table.add_column("Description", style="yellow")
        table.add_column("Streak", style="green")
        table.add_column("Reminders", style="magenta")

        for h in habits:
            streak = Habit.current_streak(h["name"])
            remind_status = "On" if h["remind"] else "Off"
            table.add_row(
                h["name"], h["category"], h["description"], str(streak), remind_status
            )
        console.print(table)

    @staticmethod
    def log(habit_name, date_str, status):
        """Logs the status of a habit for a given date."""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")
        if status not in ("completed", "missed"):
            raise ValueError("Status must be 'completed' or 'missed'.")
        database.log_status(habit_name, date_str, status)
        console.print(
            Panel(
                f"Logged status '{status}' for habit '{habit_name}' on {date_str}.",
                style="green",
            )
        )

    @staticmethod
    def get_logs(habit_name, start=None, end=None):
        """Gets the logs for a habit within a given date range."""
        return database.get_logs(habit_name, start, end)

    @staticmethod
    def set_reminder(name, remind):
        """Sets a reminder for a habit."""
        database.set_habit_attribute(name, "remind", remind)
        status = "on" if remind else "off"
        console.print(Panel(f"Reminders for '{name}' turned {status}.", style="green"))

    @staticmethod
    def archive(name):
        """Archives a habit."""
        database.set_habit_attribute(name, "archived", True)
        console.print(Panel(f"Habit '{name}' archived.", style="yellow"))

    @staticmethod
    def unarchive(name):
        """Unarchives a habit."""
        database.set_habit_attribute(name, "archived", False)
        console.print(Panel(f"Habit '{name}' unarchived.", style="green"))

    @staticmethod
    def current_streak(habit_name):
        """Calculates the current streak for a habit."""
        logs = database.get_logs(habit_name)
        if not logs:
            return 0
        history_dates = [
            datetime.strptime(d, "%Y-%m-%d").date() for d in sorted(logs.keys())
        ]
        streak = 0
        prev = date.today()
        for d in reversed(history_dates):
            if logs.get(d.isoformat()) == "completed":
                if prev == d or prev == d + timedelta(days=1):
                    streak += 1
                    prev = d
                else:
                    break
        return streak
