from cli import commands
from cli.command import Command


class ImportCommand(Command):
    """Command to import habit data."""

    def __init__(self):
        """Initializes the ImportCommand."""
        super().__init__("import", "Import habit data from CSV or JSON.")

    def configure_parser(self, parser):
        """Configures the parser for the import command."""
        parser.add_argument("name", help="Habit name")
        parser.add_argument("format", choices=["csv", "json"])
        parser.add_argument("file", help="Input file path")

    def execute(self, args):
        """Executes the import command."""
        commands.import_data(args.name, args.format, args.file)
