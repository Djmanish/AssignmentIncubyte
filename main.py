import re

class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        # Check for custom delimiter
        delimiter = ','
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        # Replace newlines with delimiter
        numbers = numbers.replace('\n', delimiter)
        
        # Split the string by delimiter and convert to integers
        num_list = re.split(delimiter, numbers)
        num_list = [int(num) for num in num_list if num]

        # Check for negative numbers
        negative_numbers = [num for num in num_list if num < 0]
        if negative_numbers:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negative_numbers))}")

        # Return the sum
        return sum(num_list)

# Unit Tests

import unittest

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_0(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,5"), 6)

    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4"), 10)

    def test_newline_as_delimiter(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -4")

if __name__ == "__main__":
    unittest.main()
