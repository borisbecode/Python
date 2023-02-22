print(len("Hello Word"))
arr = ["one", "two"]
print(len(arr))

""" 1. Create a variable count_alpha that contains the number of characters contained in the string "Hello world!". """
print(len("Hello World!"))
count_alpha = len("Hello World!")
print(count_alpha)



""" 2. Create a variable count_float and cast the variable count_alpha to float. """
count_float = float(count_alpha)

""" 3. Round the variable pi value to 2 decimal places (0.01) and save it in a variable round_pi. You can get pi from the math library. """
from math import pi
round_pi = round(pi,2)
print (round_pi)

""" 4. Create a variable reversed_text which contains the character string "Hello world!" backwards.
The result must be a list object. """    

Hello = "Hello World!"
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

reversed_text = Convert(Hello)
reversed_text.reverse()
print(reversed_text)


""" 5. Create a variable age and ask the user to enter his age. Then display it and display its type. """

age = input("quel age as tu ? :")
print(age)
print(type(age)) 

""" 6. Create a variable sorted_num that contains the sorted num list. """
sorted_num = [2, 8, 1, 4, 6, 3, 7]
print(sorted(sorted_num))

""" 7. Create a variable sum_of_list which contains the sum of all the elements in the list num. """

sum_of_list = [2, 8, 1, 4, 6, 3, 7]
print(sum(sum_of_list))

""" 8. Create a variable min_value that contains a minimum value of list num. """
min_value = [2, 8, 1, 4, 6, 3, 7]
print(min(min_value))

""" 9. Create a variable max_value that contains the maximum value of list num. """


max_value = [2, 8, 1, 4, 6, 3, 7]
print(max(max_value))

""" 10. Find a function that will interpret the string of the variable calc """
calc = "1 + 2"
string_interpret=eval(calc)
print(string_interpret)





import unittest


class TestNotebook(unittest.TestCase):
    def test_count_alpha(self):
        self.assertEqual(count_alpha, 12)

    def test_count_float(self):
        self.assertEqual(type(count_float), float)

    def test_pi(self):
        self.assertEqual(3.14, round_pi)

    def test_reversed(self):
        self.assertEqual(
            reversed_text, ["!", "d", "l", "r", "o", "w", " ", "o", "l", "l", "e", "H"]
        )

    def test_age(self):
        self.assertEqual(type(age), str)

    def test_sorted(self):
        self.assertEqual(sorted_num, [1, 2, 3, 4, 6, 7, 8])

    def test_sum(self):
        self.assertEqual(sum_of_list, 31)

    def test_min(self):
        self.assertEqual(min_value, 1)

    def test_max(self):
        self.assertEqual(max_value, 8)

    def test_interpret(self):
        self.assertEqual(string_interpret, 3)


unittest.main(argv=[""], verbosity=2, exit=False)
     

