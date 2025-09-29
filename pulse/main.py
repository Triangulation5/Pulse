import argparse
import getpass
import json
import os

from cli.add_command import AddCommand
from cli.archive_command import ArchiveCommand
from cli.backup_command import BackupCommand
from cli.command import CommandManager
from cli.delete_command import DeleteCommand
from cli.export_command import ExportCommand
from cli.import_command import ImportCommand
from cli.list_command import ListCommand
from cli.log_command import LogCommand
from cli.monthly_command import MonthlyCommand
from cli.range_command import RangeCommand
from cli.remind_off_command import RemindOffCommand
from cli.remind_on_command import RemindOnCommand
from cli.rename_command import RenameCommand
from cli.restore_command import RestoreCommand
from cli.show_command import ShowCommand
from cli.unarchive_command import UnarchiveCommand
from cli.weekly_command import WeeklyCommand
from db.database import initialize_database
from rich.console import Console
from rich.panel import Panel

initialize_database()

console = Console()

PROFILE_DIR = os.path.join(os.path.dirname(__file__), "Profiles")
PROFILE_EXT = ".json"

habit_banner = """
╔═══════════════════════════════════════════════════════╗
│                        Pulse                          │
│        Your Ultimate Habit Tracking Companion         │
╚═══════════════════════════════════════════════════════╝
"""


def list_profiles():
    if not os.path.exists(PROFILE_DIR):
        os.makedirs(PROFILE_DIR)
    return [
        f[: -len(PROFILE_DIR)]
        for f in os.listdir(PROFILE_DIR)
        if f.endswith(PROFILE_EXT)
    ]


def profile_path(name):
    return os.path.join(PROFILE_DIR, name + PROFILE_EXT)


def save_profile(profile):
    with open(profile_path(profile["name"]), "w") as f:
        json.dump(profile, f)


def load_profile(name):
    with open(profile_path(name), "r") as f:
        return json.load(f)


def create_profile():
    while True:
        name = input("New profile name: ").strip()
        if not name or any(c in name for c in '/\\:*?"<>|'):
            print("Invalid name.")
            continue
        if name in list_profiles():
            print("Profile exists.")
            continue
        password = getpass.getpass("Password: ")
        confirm = getpass.getpass("Confirm: ")
        if password != confirm:
            print("Passwords do not match.")
            continue
        profile = {"name": name, "password": password, "balance": 0, "inventory": {}}
        save_profile(profile)
        print(f'Profile "{name}" created!')
        return profile


def delete_profile():
    profiles = list_profiles()
    if not profiles:
        print("No profiles to delete.")
        return None
    while True:
        print("Profiles:")
        for idx, p in enumerate(profiles, 1):
            print(f"{idx}. {p}")
        choice = input("Select profile to delete #: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(profiles):
            name = profiles[int(choice) - 1]
        elif choice in profiles:
            name = choice
        else:
            print("Invalid.")
            continue


def authenticate_profile():
    profiles = list_profiles()
    if not profiles:
        print("No profiles. Create one.")
        return create_profile()
    while True:
        print("Profiles:")
        for idx, p in enumerate(profiles, 1):
            print(f"{idx}. {p}")
        choice = input(
            'Select profile, or type "create", "new" to create new one #: '
        ).strip()
        if choice.isdigit() and 1 <= int(choice) <= len(profiles):
            name = profiles[int(choice) - 1]
        elif choice in ("create", "new"):
            return create_profile()
        elif choice in profiles:
            name = choice
        else:
            print("Invalid.")
            continue
        password = getpass.getpass("Password: ")
        profile = load_profile(name)
        if password == profile["password"]:
            print(f"Welcome, {name}!")
            return profile
        else:
            print("Wrong password.\n")


def main():
    """The main function of the Pulse application."""
    parser = argparse.ArgumentParser(
        description=habit_banner, formatter_class=argparse.RawTextHelpFormatter
    )

    manager = CommandManager(parser)
    manager.register(AddCommand())
    manager.register(DeleteCommand())
    manager.register(WeeklyCommand())
    manager.register(MonthlyCommand())
    manager.register(RenameCommand())
    manager.register(ListCommand())
    manager.register(LogCommand())
    manager.register(ShowCommand())
    manager.register(RangeCommand())
    manager.register(RemindOnCommand())
    manager.register(RemindOffCommand())
    manager.register(ArchiveCommand())
    manager.register(UnarchiveCommand())
    manager.register(ExportCommand())
    manager.register(ImportCommand())
    manager.register(BackupCommand())
    manager.register(RestoreCommand())

    try:
        manager.run()
    except Exception as e:
        console.print(Panel(f"[bold red]Error:[/bold red] {str(e)}"))


if __name__ == "__main__":
    main()
