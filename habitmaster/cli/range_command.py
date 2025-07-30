from cli import commands
from cli.command import Command


class RangeCommand(Command):
    """Command to show a heatmap for a custom date range."""

    def __init__(self):
        """Initializes the RangeCommand."""
        super().__init__("range", "Show a heatmap for a custom date range.")

    def configure_parser(self, parser):
        """Configures the parser for the range command."""
        parser.add_argument("names", nargs="+", help="Habit names")
        parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
        parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")

    def execute(self, args):
        """Executes the range command."""
        commands.show_heatmap(args.names, start=args.start, end=args.end)
