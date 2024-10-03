# HOMEWORK - 1st task
from datetime import datetime


def get_days_from_today(date: str) -> int | str:

    if type(date) is str:
        try:
            today = datetime.today().date()
            date_in_datetime_format = datetime.strptime(date, "%Y-%m-%d").date()
            return (date_in_datetime_format - today).days
        except ValueError:
            return f"Wrong date format given: input in form \"{date}\" does not match format \"%Y-%m-%d\""

    return f"Wrong date format: {type(date)}, must be str"
