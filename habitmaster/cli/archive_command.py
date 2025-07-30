from cli import commands
from cli.command import Command


class ArchiveCommand(Command):
    """Command to archive a habit."""

    def __init__(self):
        """Initializes the ArchiveCommand."""
        super().__init__("archive", "Archive a habit.")

    def configure_parser(self, parser):
        """Configures the parser for the archive command."""
        parser.add_argument("name", help="Name of the habit")

    def execute(self, args):
        """Executes the archive command."""
        commands.archive_habit(args.name)
