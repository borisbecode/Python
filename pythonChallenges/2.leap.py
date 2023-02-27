import unittest




def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):

        print(year, "c'est une année bissextile")
        return True
    else:
        print(year, "ce n'est pas une année bissextile")
        return False

is_leap_year(1992)


class YearTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertIs(is_leap_year(1996), True)

    def test_non_leap_year(self):
        self.assertIs(is_leap_year(1997), False)

    def test_non_leap_even_year(self):
        self.assertIs(is_leap_year(1998), False)

    def test_century(self):
        self.assertIs(is_leap_year(1900), False)

    def test_exceptional_century(self):
        self.assertIs(is_leap_year(2400), True)

if __name__ == '__main__':
    unittest.main()
