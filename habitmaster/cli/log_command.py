from cli import commands
from cli.command import Command


class LogCommand(Command):
    """Command to log the status of a habit."""

    def __init__(self):
        """Initializes the LogCommand."""
        super().__init__("log", "Log the status of a habit.")

    def configure_parser(self, parser):
        """Configures the parser for the log command."""
        parser.add_argument("name", help="Name of the habit")
        parser.add_argument(
            "status", choices=["completed", "missed"], help="Daily status"
        )
        parser.add_argument(
            "--date", help="Date (YYYY-MM-DD or 'today')", default="today"
        )

    def execute(self, args):
        """Executes the log command."""
        commands.log_status(args.name, args.date, args.status)
