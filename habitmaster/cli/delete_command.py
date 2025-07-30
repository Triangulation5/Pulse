from cli import commands
from cli.command import Command


class DeleteCommand(Command):
    """Command to delete a habit."""

    def __init__(self):
        """Initializes the DeleteCommand."""
        super().__init__("delete", "Delete a habit.")

    def configure_parser(self, parser):
        """Configures the parser for the delete command."""
        parser.add_argument("name", help="Name of the habit to delete")

    def execute(self, args):
        """Executes the delete command."""
        commands.delete_habit(args.name)
