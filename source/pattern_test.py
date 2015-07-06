import unittest
from pattern import Pattern

class Pattern_test(unittest.TestCase):
    def test_load_bitmap(self):
        p = Pattern()
        self.assertRaises(FileNotFoundError, p.load_bitmap, 'blah')

if __name__ == '__main__':
    unittest.main()
