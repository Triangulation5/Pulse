from cli import commands
from cli.command import Command


class ListCommand(Command):
    """Command to list all habits."""

    def __init__(self):
        """Initializes the ListCommand."""
        super().__init__("list", "List all habits.")

    def configure_parser(self, parser):
        """Configures the parser for the list command."""
        parser.add_argument(
            "--archived", action="store_true", help="Include archived habits"
        )

    def execute(self, args):
        """Executes the list command."""
        commands.list_habits(args)
