import unittest
import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        result = []
        result.append(fizz_buzz.fizz_buzz(3))
        for output in result:
            self.assertEqual(output, "Fizz")


if __name__ == "__main__":
    unittest.main()
