from cli import commands
from cli.command import Command


class MonthlyCommand(Command):
    """Command to show a monthly summary of all habits."""

    def __init__(self):
        """Initializes the MonthlyCommand."""
        super().__init__("monthly", "Show a monthly summary of all habits.")

    def configure_parser(self, parser):
        """Configures the parser for the monthly command."""
        pass

    def execute(self, args):
        """Executes the monthly command."""
        commands.monthly_view()
