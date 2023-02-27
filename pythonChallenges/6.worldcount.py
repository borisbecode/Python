import unittest



def worldcount(sentence):
    novirgule = sentence.replace(","," ")
    nopoint = novirgule.replace(".","")
    nospace = nopoint.replace("_", " ")
    
    words = nospace.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


worldcount("jaime les ramdam ramdam dam")








# -*- coding: utf-8 -*-





# to be backwards compatible with the old Python 2.X
def decode_if_needed(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string


""" class WordCountTests(unittest.TestCase):

    def test_count_one_word(self):
        self.assertEqual(
            {'word': 1},
            worldcount('word')
        )

    def test_count_one_of_each(self):
        self.assertEqual(
            {'one': 1, 'of': 1, 'each': 1},
            worldcount('one of each')
        )

    def test_count_multiple_occurences(self):
        self.assertEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            worldcount('one fish two fish red fish blue fish')
        )

    def test_preserves_punctuation(self):
        self.assertEqual(
            {'car': 1, 'carpet': 1, 'as': 1, 'java': 1, 'javascript': 1},
            worldcount('car : carpet as java : javascript!!&@$%^&')
        )

    def test_include_numbers(self):
        self.assertEqual(
            {'testing': 2, '1': 1, '2': 1},
            worldcount('testing 1 2 testing')
        )

    def test_mixed_case(self):
        self.assertEqual(
            [2, 3],
            sorted(list(worldcount('go Go GO Stop stop').values()))
        )

    def test_multiple_spaces(self):
        self.assertEqual(
            {'wait': 1, 'for': 1, 'it': 1},
            worldcount('wait for       it')
        )

    def test_newlines(self):
        self.assertEqual(
            {'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2,
             'want': 1, 'your': 1, 'bad': 1, 'romance': 1},
            worldcount('rah rah ah ah ah\nroma roma ma\n'
                       'ga ga oh la la\nwant your bad romance')
        )

    def test_tabs(self):
        self.assertEqual(
            {'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2,
             'want': 1, 'your': 1, 'bad': 1, 'romance': 1},
            worldcount('rah rah ah ah ah\troma roma ma\tga ga oh la la\t'
                       'want your bad romance')
        )

    def test_non_alphanumeric(self):
        self.assertEqual(
            {'hey': 1, 'my': 1, 'spacebar': 1, 'is': 1, 'broken': 1},
            worldcount('hey,my_spacebar_is_broken.')
        )

    def test_unicode(self):
        self.assertEqual(
            {decode_if_needed('до'): 1, decode_if_needed('свидания'): 1},
            worldcount('до🖖свидания!')
        )

if __name__ == '__main__':
    unittest.main() """