from cli import commands
from cli.command import Command


class RestoreCommand(Command):
    """Command to restore the database."""

    def __init__(self):
        """Initializes the RestoreCommand."""
        super().__init__("restore", "Restore the database from a backup.")

    def configure_parser(self, parser):
        """Configures the parser for the restore command."""
        parser.add_argument("file", help="Backup file path")

    def execute(self, args):
        """Executes the restore command."""
        commands.restore_database(args.file)
