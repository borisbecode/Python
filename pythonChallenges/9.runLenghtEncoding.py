# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

def encode(string):
    result =""
    nombre = 1

    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            nombre += 1
        else:
            result += str(nombre) if nombre > 1 else ""
            result += string [i-1]
            nombre = 1
    result += str(nombre) if nombre > 1 else ""        
    result += string[-1]
    print(result)
    return result

encode("BWWWWWWWWWWWWBWWWWWWWWWWWWBBWWWWWWWWWWWWWWWWWWWWWWWWB")



def decode(string):
    result = ""
    nombre = ""
    for lettre in string:
        if lettre.isdigit():
            nombre += lettre
        else:
            result += lettre * (int(nombre) if nombre else 1)
            nombre = ""
    print(result)
    return result


decode("B12WB12W2B24WB")









class WordCountTests(unittest.TestCase):

    def test_encode(self):
        self.assertMultiLineEqual('2A3B4C', encode('AABBBCCCC'))

    def test_decode(self):
        self.assertMultiLineEqual('AABBBCCCC', decode('2A3B4C'))

    def test_encode_with_single(self):
        self.assertMultiLineEqual(
            '12WB12W3B24WB',
            encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'))

    def test_decode_with_single(self):
        self.assertMultiLineEqual(
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB',
            decode('12WB12W3B24WB'))

    def test_combination(self):
        self.assertMultiLineEqual('zzz ZZ  zZ', decode(encode('zzz ZZ  zZ')))

    def test_encode_unicode_s(self):
        self.assertMultiLineEqual('⏰3⚽2⭐⏰', encode('⏰⚽⚽⚽⭐⭐⏰'))

    def test_decode_unicode(self):
        self.assertMultiLineEqual('⏰⚽⚽⚽⭐⭐⏰', decode('⏰3⚽2⭐⏰'))

if __name__ == '__main__':
    unittest.main()




