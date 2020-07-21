import unittest

import time_calculator


class TestTimeFunctions(unittest.TestCase):

    def test_split_time(self):
        self.assertEqual(
            time_calculator.split_time('12:45 AM', True),
            ('12', '45', 'AM'),
        )
        self.assertEqual(
            time_calculator.split_time('99:87 PM', True),
            ('99', '87', 'PM'),
        )
        self.assertEqual(
            time_calculator.split_time('78:23'),
            ('78', '23')
        )

    def test_convert_to_24_hours(self):
        self.assertEqual(
            time_calculator.convert_to_24_hours('07:55 AM', True),
            (7, 55),
        )
        self.assertEqual(
            time_calculator.convert_to_24_hours('06:34 PM', True),
            (18, 34),
        )
        self.assertEqual(
            time_calculator.convert_to_24_hours('13:09'),
            (13, 9),
        )

    def test_normalize_duration(self):
        self.assertEqual(
            time_calculator.normalize_duration('49:24'),
            (1, 24, 2),
        )
        self.assertEqual(
            time_calculator.normalize_duration('20:20'),
            (20, 20, 0),
        )

    def test_calculate_days(self):
        self.assertEqual(
            time_calculator.calculate_days(48),
            2,
        )
        self.assertEqual(
            time_calculator.calculate_days(15),
            0,
        )
        self.assertEqual(
            time_calculator.calculate_days(25),
            1,
        )

    def test_add_times(self):
        self.assertEqual(
            time_calculator.add_times(
                (20, 20),
                (20, 20),
            ),
            (16, 40, 1),
        )
        self.assertEqual(
            time_calculator.add_times(
                (10, 50),
                (12, 20),
            ),
            (23, 10, 0),
        )

    def test_get_day(self):
        self.assertEqual(
            time_calculator.get_day('TuEsday'),
            2,
        )
        self.assertEqual(
            time_calculator.get_day('SATURDAY'),
            6,
        )

    def test_get_weekday(self):
        self.assertEqual(
            time_calculator.get_weekday(3),
            'Wednesday',
        )
        self.assertEqual(
            time_calculator.get_weekday(6),
            'Saturday',
        )

    def test_calculate_weekday(self):
        self.assertEqual(
            time_calculator.calculate_weekday(2, 8),
            3,
        )
        self.assertEqual(
            time_calculator.calculate_weekday(6, 2),
            1,
        )
    
    def test_convert_to_12_hours(self):
        self.assertEqual(
            time_calculator.convert_to_12_hours(12, 30),
            '12:30 PM',
        )
        self.assertEqual(
            time_calculator.convert_to_12_hours(0, 30),
            '12:30 AM',
        )
        self.assertEqual(
            time_calculator.convert_to_12_hours(16, 0),
            '4:00 PM',
        )
    
    def test_add_time(self):
        self.assertEqual(
            time_calculator.add_time("3:00 PM", "3:10"),
            '6:10 PM',
        )


if __name__ == '__main__':
    unittest.main()
