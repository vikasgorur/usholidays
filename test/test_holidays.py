from unittest import TestCase

from datetime import date

import usholidays


class ForYearTests(TestCase):
    def test_2019(self):
        year = 2019
        holidays = usholidays.for_year(year)
        answers = {
            "New Year's Day": date(year, 1, 1),
            "Martin Luther King Jr. Day": date(year, 1, 21),
            "Presidents' Day": date(year, 2, 18),
            "Memorial Day": date(year, 5, 27),
            "Independence Day": date(year, 7, 4),
            "Labor Day": date(year, 9, 2),
            "Columbus Day": date(year, 10, 14),
            "Veterans Day": date(year, 11, 11),
            "Thanksgiving": date(year, 11, 28),
            "Christmas": date(year, 12, 25),
        }

        for k in answers.keys():
            self.assertEqual(holidays[k], answers[k])
