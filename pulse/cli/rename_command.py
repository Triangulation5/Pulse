from cli import commands
from cli.command import Command


class RenameCommand(Command):
    """Command to rename a habit."""

    def __init__(self):
        """Initializes the RenameCommand."""
        super().__init__("rename", "Rename a habit.")

    def configure_parser(self, parser):
        """Configures the parser for the rename command."""
        parser.add_argument("old_name", help="Current habit name")
        parser.add_argument("new_name", help="New habit name")

    def execute(self, args):
        """Executes the rename command."""
        commands.rename_habit(args.old_name, args.new_name)
