import unittest
from find_divisible_number import find_divisible_number  # Assicurati che il nome dello script sia corretto


class TestFindDivisibleNumber(unittest.TestCase):
    def test_find_divisible_number(self):
        self.assertEqual(find_divisible_number(10), (True, [2, 5, 10]))

    def test_find_divisible_number_minor_2(self):
        self.assertEqual(find_divisible_number(1), (False, []))

    def test_find_divisible_number_prime(self):
        self.assertEqual(find_divisible_number(13), (True, [13]))

    def test_find_divisible_number_not_number(self):
        self.assertEqual(find_divisible_number('abc'), (False, []))
    
if __name__ == '__main__':
    unittest.main()