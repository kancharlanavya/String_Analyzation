#!/apps/TOOLS/PYTHON/bin/python

import unittest
from string_analyze import analyze_string


class MyTestCase(unittest.TestCase):
    def test_analyze_string_normal(self):
        s = analyze_string("ThisisNavys")
        self.assertRaises(Exception, s.length())

    def test_analyze_string_single_string(self):
        s = analyze_string("The cow jumped over the moon.")
        self.assertRaises(Exception, s.length())

    def test_analyze_string_nullstring(self):
        s = analyze_string("")
        self.assertRaises(Exception, s.length())

    def test_analyze_string_nostring(self):
        s = analyze_string()
        self.assertRaises(Exception, s.length())

if __name__ == '__main__':
    unittest.main()
