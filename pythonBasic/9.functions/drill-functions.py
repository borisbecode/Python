""" name = {}
name["first_name"] = "Alan"
name["last_name"] = "Turing"


def hello(first_name, last_name):
    print(f"Hello {first_name} {last_name} and welcome!")


hello(**name) """


""" 1. Say Hello """

def hello(name="Anonymous"):
    """ if len(name) == 0:
        return print("Hello Anonymous") """
    return "Hello " + name
    

hello("Boris")


""" 2. Count students """

list = [["Jean", "Alice", "Edwige", "Peter", "James"],
               ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]]
def sum_of_students(list):
    integer = 0
    for nbList in list:
        for nbStudent in nbList:
            integer += 1
    print("il y a ", integer ," d'étudiants")
    return integer

sum_of_students(list)


""" 3. Is divisible ? """

def is_divisible(n, x, y):
    """ a = float(n/x)
    b= n/y
    if a == int:
        return True
    else:
        return False  """
    if n%x ==  0 and n%y == 0: 
        return True
    else:
        return False




"""  
    if n/x == int and n/y ==int: 
        print("yes")
    else:
        print("nooo")
     """
print(is_divisible(100,5,2))



def isFirstgreater(num1,num2): 
  if num1 > num2: 
     return True 
  return False 

print(isFirstgreater(5,8))


""" 4. Abbreviate a two-word name """



def abbreviate_name(name):
    name_list = name.split()
    initials = ""
    for name in range(len(name_list)):
        initials += name_list[name][0].upper() +"."
    initials = initials[:-1]
    print(initials)
    return initials

abbreviate_name("boris elmuerte")


""" 5. Sum of positive """

def positive_sum(numbers):
    onlyPositive = [x for x in numbers if x > 0] 
    sumNumbers = sum(onlyPositive)
    print(sumNumbers)
    return sumNumbers
    

xx= [1,-4,7,12]

positive_sum(xx)


""" 6. Sum mixed array """
def mixed_sum(array):
    list_string = map(int, array) 
    Total = sum(list_string)
    print(Total)
    return Total

mixed_sum(['5', '0', 9, 3, 2, 1, '9', 6, 7])    


""" 7. Return the day """


def what_day(number):
    
    numberInt = int(number)
    Days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if number > 0 and number <= 7:
        wichDays = Days[numberInt -1]
        print(wichDays)
        return wichDays
    else:
        h = "Wrong, please enter a number between 1 and 7"
        print(h)
        return h
    
     

what_day(1)

""" 8. Summation """


def summation(number):
    n = 1
    list = []
    if number < 0:
        print('enter a number bigger than 1')
        
    while n <= number:
        list.append(n)
        n += 1
        
        x = sum(list)
        print(sum(list))
    return x
        

summation(8)



""" 9. If you can't sleep, just count sheep!! """

def count_sheep(number):
    if number < 0:
        print('enter a number bigger than 1')
    sheep = " sheep..."
    n = 1
    my_string = ""
    while n <= number:
        """ print(n,sheep) """
        x = f"{n}{sheep}"
        list = [x]
        my_string += str(x)
        """ print(my_string)
        print(f"{n}{sheep}") """
        
        
        
        n +=1
    print(my_string)
    return my_string
    
     
    
count_sheep(8)




""" 10. Student's final grade """

""" This function should return a number, i.e. the final grade. There are four types of final grades:

100, if a grade for the exam is more than 90 or if the number of completed projects more than 10.
90, if a grade for the exam is more than 75 and if the number of completed projects is minimum 5.
75, if a grade for the exam is more than 50 and if the number of completed projects is minimum 2.
0, in other cases """

def final_grade(exam_grade, completed_projects):
    if exam_grade >= 90 and completed_projects >= 10:
        print("100")
        return 100
    elif exam_grade >= 75 and completed_projects >= 5:
        print("90")
        return 90
    elif exam_grade >= 50 and completed_projects >= 2:
        print("75") 
        return 75 
    else:
        print("0")
        return 0    


final_grade(75,10)





import unittest


class TestNotebook(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello Anonymous")
        self.assertEqual(hello("Jean"), "Hello Jean")

    def test_sum_of_students(self):
        self.assertEqual(
            sum_of_students(
                [
                    ["Jean", "Alice", "Edwige", "Peter", "James"],
                    ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"],
                ]
            ),
            10,
        )

    def test_is_divisible(self):
        self.assertEqual(is_divisible(3, 3, 4), False)
        self.assertEqual(is_divisible(12, 3, 4), True)
        self.assertEqual(is_divisible(8, 3, 4), False)
        self.assertEqual(is_divisible(48, 3, 4), True)

    def test_abbreviate_name(self):
        self.assertEqual(abbreviate_name("Sam Harris"), "S.H")
        self.assertEqual(abbreviate_name("Patrick Feenan"), "P.F")
        self.assertEqual(abbreviate_name("Evan Cole"), "E.C")
        self.assertEqual(abbreviate_name("P Favuzzi"), "P.F")
        self.assertEqual(abbreviate_name("David Mendieta"), "D.M")

    def test_positive_sum(self):
        self.assertEqual(positive_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(positive_sum([1, -2, 3, 4, 5]), 13)
        self.assertEqual(positive_sum([-1, 2, 3, 4, -5]), 9)
        self.assertEqual(positive_sum([]), 0)
        self.assertEqual(positive_sum([-1, -2, -3, -4, -5]), 0)

    def test_sum_mixed_array(self):
        self.assertEqual(mixed_sum([9, 3, "7", "3"]), 22)
        self.assertEqual(mixed_sum(["5", "0", 9, 3, 2, 1, "9", 6, 7]), 42)
        self.assertEqual(mixed_sum(["3", 6, 6, 0, "5", 8, 5, "6", 2, "0"]), 41)
        self.assertEqual(mixed_sum(["1", "5", "8", 8, 9, 9, 2, "3"]), 45)
        self.assertEqual(mixed_sum([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)

    def test_return_day(self):
        self.assertEqual(what_day(1), "Sunday")
        self.assertEqual(what_day(2), "Monday")
        self.assertEqual(what_day(3), "Tuesday")
        self.assertEqual(what_day(8), "Wrong, please enter a number between 1 and 7")
        self.assertEqual(what_day(20), "Wrong, please enter a number between 1 and 7")

    def test_summation(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)

    def test_count_sheep(self):
        self.assertEqual(count_sheep(1), "1 sheep...")
        self.assertEqual(count_sheep(2), "1 sheep...2 sheep...")
        self.assertEqual(count_sheep(3), "1 sheep...2 sheep...3 sheep...")

    def test_final_grade(self):
        self.assertEqual(final_grade(100, 12), 100)
        self.assertEqual(final_grade(85, 5), 90)


unittest.main(argv=[""], verbosity=2, exit=False) 