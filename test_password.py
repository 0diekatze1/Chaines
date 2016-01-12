# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("aabbcdg"), "aabbcdh")

    def test_getNextBadChar(self):
        self.assertEqual(pwd.getNext("aabbcdh"), "aabbcdj")
        
    def test_getNextTwoPairs(self):
        self.assertEqual(pwd.getNext("abcaabb"), "abcaacc")

    def test_getNextSeries(self):
        self.assertEqual(pwd.getNext("abbaaaba"), "abbaaabc")

    def test_getNextEndList(self):
        self.assertRaises(ValueError, pwd.getNext, "zzzz")

    def test_hasSeries(self):
        self.assertTrue(pwd.hasSeries("abc"))
        self.assertFalse(pwd.hasSeries("abd"))

    def test_hasTwoPairs(self):
        self.assertTrue(pwd.hasTwoPairs("aabb"))
        self.assertFalse(pwd.hasTwoPairs("aaab"))
        self.assertFalse(pwd.hasTwoPairs("abab"))
        self.assertTrue(pwd.hasTwoPairs("aaabcc"))

    def test_hasNoBadChar(self):
        self.assertFalse(pwd.hasNoBadChar("aaoaa"))
        self.assertFalse(pwd.hasNoBadChar("oaaaa"))
        self.assertFalse(pwd.hasNoBadChar("aalaa"))
        self.assertFalse(pwd.hasNoBadChar("aaaai"))
        self.assertTrue(pwd.hasNoBadChar("aaaaa"))



# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
