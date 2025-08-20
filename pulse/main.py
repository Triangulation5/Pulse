import argparse

from cli.add_command import AddCommand
from cli.archive_command import ArchiveCommand
from cli.backup_command import BackupCommand
from cli.command import CommandManager
from cli.delete_command import DeleteCommand
from cli.export_command import ExportCommand
from cli.import_command import ImportCommand
from cli.list_command import ListCommand
from cli.log_command import LogCommand
from cli.monthly_command import MonthlyCommand
from cli.range_command import RangeCommand
from cli.remind_off_command import RemindOffCommand
from cli.remind_on_command import RemindOnCommand
from cli.rename_command import RenameCommand
from cli.restore_command import RestoreCommand
from cli.show_command import ShowCommand
from cli.unarchive_command import UnarchiveCommand
from cli.weekly_command import WeeklyCommand
from db.database import initialize_database
from rich.console import Console
from rich.panel import Panel

initialize_database()

console = Console()

habit_banner = """
╔═══════════════════════════════════════════════════════╗
│                        Pulse                          │
│        Your Ultimate Habit Tracking Companion         │
╚═══════════════════════════════════════════════════════╝
"""


def main():
    """The main function of the Pulse application."""
    parser = argparse.ArgumentParser(
        description=habit_banner, formatter_class=argparse.RawTextHelpFormatter
    )

    manager = CommandManager(parser)
    manager.register(AddCommand())
    manager.register(DeleteCommand())
    manager.register(WeeklyCommand())
    manager.register(MonthlyCommand())
    manager.register(RenameCommand())
    manager.register(ListCommand())
    manager.register(LogCommand())
    manager.register(ShowCommand())
    manager.register(RangeCommand())
    manager.register(RemindOnCommand())
    manager.register(RemindOffCommand())
    manager.register(ArchiveCommand())
    manager.register(UnarchiveCommand())
    manager.register(ExportCommand())
    manager.register(ImportCommand())
    manager.register(BackupCommand())
    manager.register(RestoreCommand())

    try:
        manager.run()
    except Exception as e:
        console.print(Panel(f"[bold red]Error:[/bold red] {str(e)}"))


if __name__ == "__main__":
    main()
