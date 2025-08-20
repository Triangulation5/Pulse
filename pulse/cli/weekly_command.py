from cli import commands
from cli.command import Command


class WeeklyCommand(Command):
    """Command to show a weekly summary of all habits."""

    def __init__(self):
        """Initializes the WeeklyCommand."""
        super().__init__("weekly", "Show a weekly summary of all habits.")

    def configure_parser(self, parser):
        """Configures the parser for the weekly command."""
        pass

    def execute(self, args):
        """Executes the weekly command."""
        commands.weekly_view()
