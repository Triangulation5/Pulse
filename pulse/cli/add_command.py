"""
Command used to add a new habit.

Usage: main.py backup [-h] out

Positional arguments:
  out         Backup file path

Options:
  -h, --help  show this help message and exit
"""

from cli import commands
from cli.command import Command


class AddCommand(Command):
    """Command to add a new habit."""

    def __init__(self):
        """Initializes the AddCommand."""
        super().__init__("add", "Add a new habit.")

    def configure_parser(self, parser):
        """Configures the parser for the add command."""
        parser.add_argument("name", help="Name of the habit")
        parser.add_argument("--category", help="Optional category for the habit")
        parser.add_argument("--description", help="Optional description for the habit")

    def execute(self, args):
        """Executes the add command."""
        commands.add_habit(args.name, args.category, args.description)
