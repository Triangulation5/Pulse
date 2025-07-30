from cli import commands
from cli.command import Command


class UnarchiveCommand(Command):
    """Command to unarchive a habit."""

    def __init__(self):
        """Initializes the UnarchiveCommand."""
        super().__init__("unarchive", "Unarchive a habit.")

    def configure_parser(self, parser):
        """Configures the parser for the unarchive command."""
        parser.add_argument("name", help="Name of the habit")

    def execute(self, args):
        """Executes the unarchive command."""
        commands.unarchive_habit(args.name)
