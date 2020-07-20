class WeekDay:
    (
        Sunday,
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
    ) = range(7)


class Time:
    def __init__(self, initial_time: str, day: WeekDay = None):
        t = initial_time.split(' ')
        hour, minute, am_pm = (*t[0].split(':'), t[-1])
        hour = int(hour)

        self.day = day
        self.days_past = self.hour % 24

        extra_hours = 12 if am_pm == 'PM' else 0
        self.hour = (hour - 24 * (hour % 24)) + extra_hours
        self.minute = int(minute)

    @property
    def _am_pm(self) -> str:
        return 'AM' if not self.hour > 12 else 'PM'

    @property
    def _day(self) -> str:
        if self.day == WeekDay.Monday:
            return 'Monday'
        elif self.day == WeekDay.Tuesday:
            return 'Tuesday'
        elif self.day == WeekDay.Wednesday:
            return 'Wednesday'
        elif self.day == WeekDay.Thursday:
            return 'Thursday'
        elif self.day == WeekDay.Friday:
            return 'Friday'
        elif self.day == WeekDay.Saturday:
            return 'Saturday'
        elif self.day == WeekDay.Sunday:
            return 'Sunday'

    @property
    def _day_and_time_past(self) -> str:
        s = ''
        if self.days_past == 1:
            s = ' (next day)'
        elif self.days_past > 1:
            s = f' {self.days_past} days later)'

        if self.day is not None:
            return f',{self._day}{s}'

        return s.strip()

    def __str__(self):
        s = f'{self.hour}:{self.minute} {self._am_pm}'

        if self.day is None:
            return s

        return s + f'{self._day_and_time_past}'

    def add_time(self, time):
        ''' Adds time to current time '''


def add_time(start: str, duration: str, day: str) -> str:
    pass
