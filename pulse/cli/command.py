"""
Includes the base class that for all the commands.
"""

from rich.console import Console
from cli.

console = Console()


class Command:
    """A base class for all commands."""

    def __init__(self, name, help_text):
        self.name = name
        self.help_text = help_text

    def configure_parser(self, parser):
        """A place to add arguments for this specific command."""
        pass

    def execute(self, args):
        """The logic to run when the command is called."""
        raise NotImplementedError("You must implement the execute method.")


class CommandManager:
    """The engine that registers and runs commands."""

    def __init__(self, parser):
        self.parser = parser
        self.subparsers = parser.add_subparsers(dest="command", required=True)
        self.commands = {}

    def register(self, command):
        """Registers a command, making it available to the CLI."""
        self.commands[command.name] = command
        command_parser = self.subparsers.add_parser(
            command.name, help=command.help_text
        )
        command.configure_parser(command_parser)

    def run(self):
        """Parses arguments and runs the chosen command."""
        args = self.parser.parse_args()
        if args.command in self.commands:
            self.commands[args.command].execute(args)
        else:
            console.print(f"[bold red]Unknown command:[/bold red] {args.command}")
            self.show_menu()

    def show_menu(self):
        """Displays a Rich-powered menu of available commands."""
        from rich.table import Table

        table = Table(
            title="HabitMaster CLI Commands",
            show_header=True,
            header_style="bold magenta",
        )
        table.add_column("Command", style="cyan", no_wrap=True)
        table.add_column("Description", style="white")
        for cmd in self.commands.values():
            table.add_row(cmd.name, cmd.help_text)
        console.print(table)
