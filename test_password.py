# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcd"), "abce")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")

    def test_getNextEndList(self):
        self.assertRaises(ValueError, pwd.getNext, "zzzz")

    def test_getNextInvalid(self):



# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
