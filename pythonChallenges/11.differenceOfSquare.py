import unittest




def square_of_sum(n):
    square_of_sums = 0
    for i in range(1, n+1):
        square_of_sums += i
    expo = square_of_sums **2   
    print(expo)
    return expo






def sum_of_squares(x):
    total = 0
    for i in range(x):
        
        total += (i+1)**2
    return total


def difference(a,b):
    return square_of_sum(a) - sum_of_squares(b)



class DifferenceOfSquaresTest(unittest.TestCase):

    def test_square_of_sum_5(self):
        self.assertEqual(225, square_of_sum(5))

    def test_sum_of_squares_5(self):
        self.assertEqual(55, sum_of_squares(5))

    def test_difference_5(self):
        self.assertEqual(170, difference(5))

    def test_square_of_sum_100(self):
        self.assertEqual(25502500, square_of_sum(100))

    def test_sum_of_squares_100(self):
        self.assertEqual(338350, sum_of_squares(100))

    def test_difference_100(self):
        self.assertEqual(25164150, difference(100))


if __name__ == '__main__':
    unittest.main()