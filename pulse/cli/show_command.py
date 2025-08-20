from cli import commands
from cli.command import Command


class ShowCommand(Command):
    """Command to show a heatmap for one or more habits."""

    def __init__(self):
        """Initializes the ShowCommand."""
        super().__init__("show", "Show a heatmap for one or more habits.")

    def configure_parser(self, parser):
        """Configures the parser for the show command."""
        parser.add_argument("names", nargs="+", help="Habit names to display")

    def execute(self, args):
        """Executes the show command."""
        commands.show_heatmap(args.names)
