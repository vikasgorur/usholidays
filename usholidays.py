import calendar
from datetime import date, timedelta

import collections


class YearMonth:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month

        # first, second, third or fourth
        self.which = None

        # monday = 1, tue = 2, ...
        self.day_of_week = None

    def _compute_date(self):
        which = 0

        if self.which == -1:
            # Count backwards from the end
            day = date(
                self.year,
                self.month,
                calendar.monthrange(self.year, self.month)[1]
            )
            delta = -1
            self.which = 1
        else:
            day = date(self.year, self.month, 1)
            delta = 1

        for i in range(31):
            if day.isoweekday() == self.day_of_week:
                which += 1

            if which == self.which:
                return day

            day = day + timedelta(days=delta)

    def first(self):
        self.which = 1
        return self

    def second(self):
        self.which = 2
        return self

    def third(self):
        self.which = 3
        return self

    def fourth(self):
        self.which = 4
        return self

    def last(self):
        self.which = -1
        return self

    def monday(self):
        self.day_of_week = 1
        return self._compute_date()

    def thursday(self):
        self.day_of_week = 4
        return self._compute_date()


def mlk_day(year: int) -> date:
    return YearMonth(year, 1).third().monday()


def presidents_day(year: int) -> date:
    return YearMonth(year, 2).third().monday()


def memorial_day(year: int) -> date:
    return YearMonth(year, 5).last().monday()


def labor_day(year: int) -> date:
    return YearMonth(year, 9).first().monday()


def columbus_day(year: int) -> date:
    return YearMonth(year, 10).second().monday()


def thanksgiving(year: int) -> date:
    return YearMonth(year, 11).fourth().thursday()


def for_year(year: int):
    return collections.OrderedDict([
        ("New Year's Day", date(year, 1, 1)),
        ("Martin Luther King Jr. Day", mlk_day(year)),
        ("Presidents' Day", presidents_day(year)),
        ("Memorial Day", memorial_day(year)),
        ("Independence Day", date(year, 7, 4)),
        ("Labor Day", labor_day(year)),
        ("Columbus Day", columbus_day(year)),
        ("Veterans Day", date(year, 11, 11)),
        ("Thanksgiving", thanksgiving(year)),
        ("Christmas", date(year, 12, 25))
    ])
