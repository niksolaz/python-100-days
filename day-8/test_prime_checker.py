import unittest
from prime_checker import prime_checker  # Assicurati che il nome dello script sia corretto


class TestPrimeChecker(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(prime_checker(5), (True, []))
    
    def test_not_prime_number(self):
        self.assertEqual(prime_checker(4), (False, [2]))

    def test_not_number(self):
        self.assertEqual(prime_checker("ciao"), (False, []))

    def test_minore_di_due(self):
        self.assertEqual(prime_checker(1), (False, []))

    def test_numero_negativo(self):
        self.assertEqual(prime_checker(-1), (False, []))

if __name__ == '__main__':
    unittest.main()