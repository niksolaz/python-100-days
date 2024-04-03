import unittest
from quicksort import quicksort

class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([3,6,8,10,1,2,1]), [1, 1, 2, 3, 6, 8, 10])
    
    def test_quicksort_alphabet(self):
        self.assertEqual(quicksort(["z", "a", "b", "c", "d", "e", "f"]), ["a", "b", "c", "d", "e", "f", "z"])


if __name__ == '__main__':
    unittest.main()

# python -m unittest test_quicksort.py