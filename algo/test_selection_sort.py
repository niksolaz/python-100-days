import unittest
from selection_sort import selection_sort 


class TestSelectionSort(unittest.TestCase):
    def test_sort_positive_number(self):
        self.assertEqual(selection_sort([5, 3, 6, 2, 10]), ([2, 3, 5, 6, 10]))

    def test_sort_negative_number(self):
        self.assertEqual(selection_sort([-5, -3, 6, 2, 10]), ([-5, -3, 2, 6, 10]))

    def test_sort_letter(self):
        self.assertEqual(selection_sort(['b', 'g', 'a']), (['a', 'b', 'g']))

    def test_sort_mixed(self):
        self.assertEqual(selection_sort(['b', 'g', 'a', 'c', 'd']), (['a', 'b', 'c', 'd', 'g']))

    def test_sort_empty(self):
        self.assertEqual(selection_sort([]), ([]))

    def test_sort_one_element(self):
        self.assertEqual(selection_sort([1]), ([1]))

    def test_not_sort_mixed_types(self):
        self.assertEqual(selection_sort([1, 'a', 2]), (False))
    
if __name__ == '__main__':
    unittest.main()