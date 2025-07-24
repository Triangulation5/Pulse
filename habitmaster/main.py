import argparse
from cli import commands
from db.database import initialize_database
from rich.console import Console
from rich.panel import Panel

initialize_database()

console = Console()

habit_banner = """
╭───────────────────────────────────────────────────────╮
│                      HabitMaster                      │
│        Your Ultimate Habit Tracking Companion         │
╰───────────────────────────────────────────────────────╯
"""

def main():
    parser = argparse.ArgumentParser(
        description=habit_banner, formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new habit")
    add_parser.add_argument("name", help="Name of the habit")
    add_parser.add_argument("--category", help="Optional category for the habit")
    add_parser.add_argument("--description", help="Optional description for the habit")

    delete_parser = subparsers.add_parser("delete", help="Delete a habit")
    delete_parser.add_argument("name", help="Name of the habit to delete")

    rename_parser = subparsers.add_parser("rename", help="Rename a habit")
    rename_parser.add_argument("old_name", help="Current habit name")
    rename_parser.add_argument("new_name", help="New habit name")

    list_parser = subparsers.add_parser("list", help="List all habits")
    list_parser.add_argument("--archived", action="store_true", help="Include archived habits")

    log_parser = subparsers.add_parser("log", help="Log daily habit status")
    log_parser.add_argument("name", help="Habit name")
    log_parser.add_argument("status", choices=["completed", "missed"], help="Daily status")
    log_parser.add_argument("--date", help="Date (YYYY-MM-DD or 'today')", default="today")

    show_parser = subparsers.add_parser(
        "show", help="Show heatmap for one or more habits"
    )
    show_parser.add_argument("names", nargs="+", help="Habit names to display")

    range_parser = subparsers.add_parser(
        "range", help="Show heatmap for custom date range"
    )
    range_parser.add_argument("names", nargs="+", help="Habit names")
    range_parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    range_parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")

    remind_on_parser = subparsers.add_parser("remind-on", help="Enable reminders for a habit")
    remind_on_parser.add_argument("name", help="Name of the habit")

    remind_off_parser = subparsers.add_parser("remind-off", help="Disable reminders for a habit")
    remind_off_parser.add_argument("name", help="Name of the habit")

    archive_parser = subparsers.add_parser("archive", help="Archive a habit")
    archive_parser.add_argument("name", help="Name of the habit")

    unarchive_parser = subparsers.add_parser("unarchive", help="Unarchive a habit")
    unarchive_parser.add_argument("name", help="Name of the habit")

    weekly_parser = subparsers.add_parser("weekly", help="Show weekly summary")
    monthly_parser = subparsers.add_parser("monthly", help="Show monthly summary")

    export_parser = subparsers.add_parser(
        "export", help="Export habit data to CSV or JSON"
    )
    export_parser.add_argument("name", help="Habit name")
    export_parser.add_argument("format", choices=["csv", "json"])
    export_parser.add_argument("out", help="Output file path")

    import_parser = subparsers.add_parser(
        "import", help="Import habit data from CSV or JSON"
    )
    import_parser.add_argument("name", help="Habit name")
    import_parser.add_argument("format", choices=["csv", "json"])
    import_parser.add_argument("file", help="Input file path")

    backup_parser = subparsers.add_parser("backup", help="Backup the database")
    backup_parser.add_argument("out", help="Backup file path")

    restore_parser = subparsers.add_parser(
        "restore", help="Restore the database from a backup"
    )
    restore_parser.add_argument("file", help="Backup file path")

    args = parser.parse_args()

    try:
        match args.command:
            case "add":
                commands.add_habit(args.name, args.category, args.description)
            case "delete":
                commands.delete_habit(args.name)
            case "rename":
                commands.rename_habit(args.old_name, args.new_name)
            case "list":
                commands.list_habits(args)
            case "log":
                commands.log_status(args.name, args.date, args.status)
            case "show":
                commands.show_heatmap(args.names)
            case "range":
                commands.show_heatmap(args.names, start=args.start, end=args.end)
            case "remind-on":
                commands.set_reminder(args.name, True)
            case "remind-off":
                commands.set_reminder(args.name, False)
            case "archive":
                commands.archive_habit(args.name)
            case "unarchive":
                commands.unarchive_habit(args.name)
            case "weekly":
                commands.weekly_view(args)
            case "monthly":
                commands.monthly_view(args)
            case "export":
                commands.export_data(args.name, args.format, args.out)
            case "import":
                commands.import_data(args.name, args.format, args.file)
            case "backup":
                commands.backup_database(args.out)
            case "restore":
                commands.restore_database(args.file)
            case _:
                console.print(Panel("[red]Unknown command[/red]"))
    except Exception as e:
        console.print(Panel(f"[bold red]Error:[/bold red] {str(e)}"))


if __name__ == "__main__":
    main()
