import unittest
import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        result = fizz_buzz.fizz_buzz()
        i = 1
        for element in result:
            if i % 3 == 0 and i % 5 != 0:
                self.assertEqual(element, "Fizz")
            i += 1

    def test_buzz(self):
        result = fizz_buzz.fizz_buzz()
        i = 1
        for element in result:
            if i % 5 == 0 and i % 3 != 0:
                self.assertEqual(element, "Buzz")
            i += 1

    def test_fizz_buzz(self):
        result = fizz_buzz.fizz_buzz()
        i = 1
        for element in result:
            if i % 3 == 0 and i % 5 == 0:
                self.assertEqual(element, "FizzBuzz")
            i += 1

    def test_numbers(self):
        result = fizz_buzz.fizz_buzz()
        i = 1
        for element in result:
            if i % 3 != 0 and i % 5 != 0:
                self.assertEqual(element, i)
            i += 1


if __name__ == "__main__":
    unittest.main()
