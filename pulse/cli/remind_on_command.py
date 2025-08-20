from cli import commands
from cli.command import Command


class RemindOnCommand(Command):
    """Command to enable reminders for a habit."""

    def __init__(self):
        """Initializes the RemindOnCommand."""
        super().__init__("remind-on", "Enable reminders for a habit.")

    def configure_parser(self, parser):
        """Configures the parser for the remind-on command."""
        parser.add_argument("name", help="Name of the habit")

    def execute(self, args):
        """Executes the remind-on command."""
        commands.set_reminder(args.name, True)
