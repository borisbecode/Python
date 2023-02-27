from __future__ import unicode_literals
import unittest


def Hello(name=""):
    if name != "":
        return f"Hello, {name}!"
    else:
        return f"Hello, World!"

Hello()    





# -*- coding: utf-8 -*-



class HelloWorldTests(unittest.TestCase):

    def test_hello_without_name(self):
        self.assertEqual(
            'Hello, World!',
            Hello()
        )

    def test_hello_with_sample_name(self):
        self.assertEqual(
            'Hello, Alice!',
            Hello('Alice')
        )

    def test_hello_with_other_sample_name(self):
        self.assertEqual(
            'Hello, Bob!',
            Hello('Bob')
        )

    def test_hello_with_umlaut_name(self):
        self.assertEqual(
            'Hello, Jürgen!',
            Hello('Jürgen')
        )

if __name__ == '__main__':
    unittest.main()


