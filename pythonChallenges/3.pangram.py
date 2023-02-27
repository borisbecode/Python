
import string
import unittest



def pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for lettre in alphabet:
        if lettre not in phrase.lower():
            print("ce n'est pas un pangramme")
            return False
    print("cest un pangramme")    
    return True

pangram('the quik brown fox jumps over the lazy dog')


# -*- coding: utf-8 -*-




class PangramTests(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(pangram(''))

    def test_valid_pangram(self):
        self.assertTrue(
            pangram('the quick brown fox jumps over the lazy dog'))

    def test_invalid_pangram(self):
        self.assertFalse(
            pangram('the quick brown fish jumps over the lazy dog'))

    def test_missing_x(self):
        self.assertFalse(pangram('a quick movement of the enemy will '
                                    'jeopardize five gunboats'))

    def test_mixedcase_and_punctuation(self):
        self.assertTrue(pangram('"Five quacking Zephyrs jolt my wax bed."'))

    def test_unchecked_german_umlaute(self):
        self.assertTrue(pangram('Victor jagt zwölf Boxkämpfer quer über den'
                                   ' großen Sylter Deich.'))


if __name__ == '__main__':
    unittest.main()