import unittest
from recursive import recursive

class TestRecursive(unittest.TestCase):
 def test_recursive(self):
       self.assertEqual(recursive(5), 15)


if __name__ == '__main__':
    unittest.main()

# python -m unittest test_recursive.py