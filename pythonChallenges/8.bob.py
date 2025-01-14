# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest



def hey(sentence):
    isaquestion =''

    if sentence != '':
        isaquestion = sentence[-1]
    
    if sentence.isupper() == True :
        print('Whoa, chill out!')
        return 'Whoa, chill out!'
    

    elif sentence =='' or sentence =='    \t':
        print('Fine. Be that way!')
        return 'Fine. Be that way!'
    
    elif sentence != "" and sentence.strip()[-1] == '?':
        print('Sure.')
        return 'Sure.'
        
    elif isaquestion == "?" :
        print('Sure.')
        return 'Sure.'
    
    
   
    
    else:
        print('Whatever.')
        return 'Whatever.'




hey("coucou?")











class BobTests(unittest.TestCase):

    def test_stating_something(self):
        self.assertEqual(
            'Whatever.',
            hey('Tom-ay-to, tom-aaaah-to.')
        )

    def test_shouting(self):
        self.assertEqual(
            'Whoa, chill out!',
            hey('WATCH OUT!')
        )

    def test_asking_a_question(self):
        self.assertEqual(
            'Sure.',
            hey('Does this cryogenic chamber make me look fat?')
        )

    def test_asking_a_numeric_question(self):
        self.assertEqual(
            'Sure.',
            hey('You are, what, like 15?')
        )

    def test_talking_forcefully(self):
        self.assertEqual(
            'Whatever.',
            hey("Let's go make out behind the gym!")
        )

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            'Whatever.', hey("It's OK if you don't want to go to the DMV.")
        )

    def test_forceful_questions(self):
        self.assertEqual(
            'Whoa, chill out!', hey('WHAT THE HELL WERE YOU THINKING?')
        )

    def test_shouting_numbers(self):
        self.assertEqual(
            'Whoa, chill out!', hey('1, 2, 3 GO!')
        )

    def test_only_numbers(self):
        self.assertEqual(
            'Whatever.', hey('1, 2, 3')
        )

    def test_question_with_only_numbers(self):
        self.assertEqual(
            'Sure.', hey('4?')
        )

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            'Whoa, chill out!',
            hey('ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!')
        )

    def test_shouting_with_umlauts(self):
        self.assertEqual(
            'Whoa, chill out!', hey('ÜMLÄÜTS!')
        )

    def test_calmly_speaking_with_umlauts(self):
        self.assertEqual(
            'Whatever.', hey('ÜMLäÜTS!')
        )

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(
            'Whoa, chill out!', hey('I HATE YOU')
        )

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            'Whatever.', hey('Ending with ? means a question.')
        )

    def test_prattling_on(self):
        self.assertEqual(
            'Sure.', hey("Wait! Hang on. Are you going to be OK?")
        )

    def test_silence(self):
        self.assertEqual(
            'Fine. Be that way!', hey('')
        )

    def test_prolonged_silence(self):
        self.assertEqual(
            'Fine. Be that way!', hey('    \t')
        )

    def test_starts_with_whitespace(self):
        self.assertEqual(
            'Whatever.', hey('         hmmmmmmm...')
        )

    def test_ends_with_whitespace(self):
        self.assertEqual(
            'Sure.', hey('What if we end with whitespace?   ')
        )

if __name__ == '__main__':
    unittest.main() 