from typing import Tuple

WEEK_DAYS = {
    'sunday': 0,
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
}


def split_time(time: str, am_pm: bool = False) -> Tuple:
    ''' Returns a `tuple` of `str` of the following values:\n
    index 0 -> hours\n
    index 1 -> minutes\n
    index 2 -> `AM` or `PM` if `am_pm` set to `True`'''
    if am_pm:
        t = time.split(' ')
        return *t[0].split(':'), t[-1]

    return *time.split(':'),


def convert_to_24_hours(time: str, am_pm: bool = False) -> Tuple[int, int]:
    if am_pm:
        hours, minutes, am_pm = split_time(time, am_pm)
        hours_to_add = 12 if am_pm == 'PM' else 0
    else:
        hours, minutes = split_time(time)
        hours_to_add = 0
    hours = int(hours) + hours_to_add
    return hours, int(minutes)


def normalize_duration(duration: str) -> Tuple[int, int, int]:
    hours, minutes = duration.split(':')
    hours = int(hours)
    normalized_hours = hours % 24
    days = calculate_days(hours)
    return (
        *convert_to_24_hours(f'{normalized_hours}:{minutes:0>2}'),
        days,
    )


def calculate_days(hours: int) -> int:
    return hours // 24


def add_times(
    time1: Tuple[int, int],
    time2: Tuple[int, int],
) -> Tuple[int, int, int]:
    added_hours = time1[0] + time2[0]
    added_minutes = time1[1] + time2[1]
    added_time = normalize_duration(f'{added_hours:0>2}:{added_minutes:0>2}')
    if added_time[1] < 60:
        return added_time
    return normalize_duration(
        f'{added_time[0] + 1}:{added_time[1] - 60:0>2}'
    )


def get_day(day: str) -> int:
    return WEEK_DAYS[day.lower()]


def get_weekday(day: int) -> str:
    for key, value in WEEK_DAYS.items():
        if value == day:
            return key.capitalize()


def calculate_weekday(current_day: int, days: int) -> int:
    return (current_day + days) % 7


def convert_to_12_hours(hours: int, minutes: int) -> str:
    if 0 <= hours <= 11:
        am_pm = 'AM'
    else:
        am_pm = 'PM'

    if hours > 12:
        hours -= 12
    elif hours == 0:
        hours += 12

    return f'{hours}:{minutes:0>2} {am_pm}'


def add_time(start: str, duration: str, day: str = None) -> str:
    start_24_hours = convert_to_24_hours(start, True)
    duration_24_hours = normalize_duration(duration)
    duration_days = calculate_days(int(split_time(duration)[0]))

    hours, minutes, days = add_times(start_24_hours, duration_24_hours[:2])
    days += duration_days
    new_time = convert_to_12_hours(hours, minutes)

    days_later = ''
    if days == 1:
        days_later = ' (next day)'
    elif days > 1:
        days_later = f' ({days} days later)'

    if day is not None:
        new_day = get_weekday(calculate_weekday(get_day(day), days))
        new_day = ', ' + new_day
        return f'{new_time}{new_day}{days_later}'

    return f'{new_time}{days_later}'
