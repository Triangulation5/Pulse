import argparse


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
            print(f"Unknown command: {args.command}")
