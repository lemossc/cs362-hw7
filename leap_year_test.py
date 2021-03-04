import unittest
import leap_year


class TestLeapYear(unittest.TestCase):
    def test_leap_years(self):
        result = leap_year.is_leap_year(2000)
        self.assertEqual(result, True)
        result = leap_year.is_leap_year(2004)
        self.assertEqual(result, True)

    def test_common_years(self):
        result = leap_year.is_leap_year(2001)
        self.assertEqual(result, False)
        result = leap_year.is_leap_year(2100)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
