# HabitMaster

<!--toc:start-->
- [HabitMaster](#habitmaster)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)
<!--toc:end-->

HabitMaster is a command-line interface (CLI) application designed to help users track and manage their habits effectively. It provides various commands to add, log, list, and analyze habits, promoting consistency and personal growth.

## Features

- **Add Habits**: Easily create new habits with customizable names and descriptions.
- **Log Progress**: Mark habits as completed for specific dates.
- **List Habits**: View all your habits and their current status.
- **Show Details**: Get detailed information about a specific habit, including its history.
- **Monthly/Weekly View**: See your habit progress over monthly and weekly periods.
- **Backup/Restore**: Securely backup and restore your habit data.
- **Export Data**: Export your habit data for external analysis.
- **Reminders**: Set up reminders for your habits.
- **Rename/Archive/Delete**: Manage your habits by renaming, archiving, or deleting them.

## Installation

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/HabitMaster.git
    cd HabitMaster
    ```

2.  **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

HabitMaster is a CLI application. You can run commands using `python habitmaster/main.py <command> [arguments]`.

Here are some basic examples:

```bash
# Add a new habit
python habitmaster/main.py add "Drink Water" --description "Drink 8 glasses of water daily"

# Log completion for a habit today
python habitmaster/main.py log "Drink Water"

# List all habits
python habitmaster/main.py list

# Show details for a specific habit
python habitmaster/main.py show "Drink Water"
```

For a full list of commands and their options, run:

```bash
python habitmaster/main.py --help
```

## Roadmap

Here are some features and improvements planned for future releases:

-   **Data Visualization**: More advanced charts and graphs to visualize habit progress over time.
-   **Web Interface**: A simple web-based interface for managing habits.
-   **Integration with Calendar Apps**: Sync habit reminders with external calendar applications.
-   **Customizable Reminders**: More flexible reminder options (e.g., specific days of the week, multiple times a day).
-   **Habit Streaks**: Track and display current and longest habit streaks.
-   **Goal Setting**: Allow users to set specific goals for their habits (e.g., complete a habit 5 times a week).

## Contributing

Contributions are welcome! Please see the `CONTRIBUTING.md` for details on how to contribute.

## License

This project is licensed under the [MIT License](LICENSE).
