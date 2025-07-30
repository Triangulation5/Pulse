from cli import commands
from cli.command import Command


class ExportCommand(Command):
    """Command to export habit data."""

    def __init__(self):
        """Initializes the ExportCommand."""
        super().__init__("export", "Export habit data to CSV or JSON.")

    def configure_parser(self, parser):
        """Configures the parser for the export command."""
        parser.add_argument("name", help="Habit name")
        parser.add_argument("format", choices=["csv", "json"])
        parser.add_argument("out", help="Output file path")

    def execute(self, args):
        """Executes the export command."""
        commands.export_data(args.name, args.format, args.out)
