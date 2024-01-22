import unittest
from prime_checker import prime_checker  # Assicurati che il nome dello script sia corretto


class TestPrimeChecker(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(prime_checker(5), (True, []))

    def test_non_prime_number(self):
        self.assertEqual(prime_checker(4), (False, [2]))

    def test_one(self):
        self.assertEqual(prime_checker(1), (False, []))

    def test_zero(self):
        self.assertEqual(prime_checker(0), (False, []))

    def test_negative_number(self):
        self.assertEqual(prime_checker(-3), (False, []))

if __name__ == '__main__':
    unittest.main()