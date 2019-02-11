"""    
Function tests

To run tests:
    python3 -m unittest <path/to/tests.py>
"""

import unittest

import functions

class TestFuncs(unittest.TestCase):

        def setUp(self):
            self.string = "#oo#o#oo##oooooo###ooo###"
            self.zeroth = 0
            self.rules = [
                         "ooo##",
                         "oo#oo",
                         "o#ooo",
                         "o#o#o",
                         "o#o##",
                         "o##oo",
                         "o####",
                         "#o#o#",
                         "#o###",
                         "##o#o",
                         "##o##",
                         "###oo",
                         "###o#",
                         "####o",
                         ]


        def test_count(self):
            self.assertEqual(functions.count("#o#o#", 0, "#"), 6)
            self.assertEqual(functions.count("#o#o#", 3, "#"), -3)
            self.assertEqual(functions.count("o#oooo##oooo#####ooo#######oooo#o#oo##o", 3, "#"), 325)


        def test_extend_string(self):
            self.assertEqual(functions.extend_string("###", 0, "#", "o"), ("ooooo###ooooo", 5))
            self.assertEqual(functions.extend_string("o###o", 0, "#", "o"), ("ooooo###ooooo", 4))


        def test_define_region(self):
            self.assertEqual(functions.define_region(self.string, 10), "##ooo")


        def test_reduce_string(self):
            self.assertEqual(functions.reduce_string("oooooooooo###oooooooooo", 10, "#", "o"), ("ooooo###ooooo", 5))


        def test_update(self):
            self.assertEqual(functions.update("##o##", self.rules), "oo#oo")
            self.assertEqual(functions.update("##o###o##o##", ["##o##"]), "oo#ooo#oo#oo")

            self.string, self.zeroth = functions.extend_string(self.string, self.zeroth, "#", "o")
            self.assertEqual(functions.update(self.string, self.rules), "ooooo#ooo#oooo#ooooo#oo#oo#oo#ooooo")


        def tearDown(self):
            del self.string
            del self.zeroth
            del self.rules