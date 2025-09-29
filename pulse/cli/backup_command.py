"""
Command to backup the database.

Usage: main.py backup [-h] out

Positional arguments:
  out         Backup file path

Options:
  -h, --help  show this help message and exit
"""
from cli import commands
from cli.command import Command


class BackupCommand(Command):
    """Command to backup the database."""

    def __init__(self):
        """Initializes the BackupCommand."""
        super().__init__("backup", "Backup the database.")

    def configure_parser(self, parser):
        """Configures the parser for the backup command."""
        parser.add_argument("out", help="Backup file path")

    def execute(self, args):
        """Executes the backup command."""
        commands.backup_database(args.out)
