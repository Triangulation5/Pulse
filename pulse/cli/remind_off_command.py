from cli import commands
from cli.command import Command


class RemindOffCommand(Command):
    """Command to disable reminders for a habit."""

    def __init__(self):
        """Initializes the RemindOffCommand."""
        super().__init__("remind-off", "Disable reminders for a habit.")

    def configure_parser(self, parser):
        """Configures the parser for the remind-off command."""
        parser.add_argument("name", help="Name of the habit")

    def execute(self, args):
        """Executes the remind-off command."""
        commands.set_reminder(args.name, False)
