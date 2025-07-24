from datetime import date, timedelta

from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich.table import Table
from rich.text import Text

console = Console()

STYLE_COMPLETED = Style(color="#30a14e")
STYLE_MISSED = Style(color="#e5534b")
STYLE_EMPTY = Style(color="bright_black", dim=True)


def daterange(start_date, end_date):
    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=1)


def week_start(d):
    return d - timedelta(days=d.weekday())


def build_heatmap(habits_data, start_date=None, end_date=None):
    today = date.today()
    if start_date is None:
        start_date = date(today.year, 1, 1)
    if end_date is None:
        end_date = today
    if end_date < start_date:
        raise ValueError("end_date must be after start_date")

    start_monday = week_start(start_date)
    end_sunday = week_start(end_date) + timedelta(days=6)

    weeks = []
    current_week_start = start_monday
    while current_week_start <= end_sunday:
        weeks.append([current_week_start + timedelta(days=i) for i in range(7)])
        current_week_start += timedelta(days=7)

    table = Table.grid(expand=True)
    habit_names = list(habits_data.keys())
    for habit in habit_names:
        table.add_column(justify="center", no_wrap=True)

    table.add_row(*[f"[bold]{habit}[/bold]" for habit in habit_names])

    for day_index in range(7):
        row_cells = []
        for habit in habit_names:
            data = habits_data[habit]
            day_cells = []
            for week in weeks:
                dt = week[day_index]
                dt_str = dt.isoformat()
                status = data.get(dt_str, None)
                if status == "completed":
                    day_cells.append(Text("■", style=STYLE_COMPLETED))
                elif status == "missed":
                    day_cells.append(Text("■", style=STYLE_MISSED))
                else:
                    day_cells.append(Text("■", style=STYLE_EMPTY))
            row_cells.append(Text("").join(day_cells))
        table.add_row(*row_cells)

    legend = Table.grid()
    legend.add_column()
    legend.add_row(Text("■ Completed", style=STYLE_COMPLETED))
    legend.add_row(Text("■ Missed", style=STYLE_MISSED))
    legend.add_row(Text("■ No Data", style=STYLE_EMPTY))

    panel = Panel.fit(
        table, title="Habit Heatmap", subtitle="Green=Completed Red=Missed Gray=No Data"
    )
    console.print(panel)
    console.print(legend)
