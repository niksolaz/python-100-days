import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 4)
    
    def test_binary_search_negative(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)

    def test_binary_search_empty(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_binary_search_one_element(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_binary_search_negative_number(self):
        self.assertEqual(binary_search([-5, -3, 6, 2, 10], -5), 0)

    def test_binary_search_letter(self):
        self.assertEqual(binary_search(['b', 'g', 'a'], 'g'), 1)

    def test_binary_search_mixed(self):
        self.assertEqual(binary_search(['b', 'g', 'a', 'c', 'd'], 'c'), 2)

    def test_binary_search_mixed_types(self):
        self.assertEqual(binary_search([1, 'a', 2], 'a'), -1)


if __name__ == '__main__':
    unittest.main()

# python -m unittest test_binary_search.py