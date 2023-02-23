""" name = {}
name["first_name"] = "Alan"
name["last_name"] = "Turing"


def hello(first_name, last_name):
    print(f"Hello {first_name} {last_name} and welcome!")


hello(**name) """


""" 1. Say Hello """

def Hello(name):
    print("Hello",name)

Hello("Boris")


""" 2. Count students """

list = [["Jean", "Alice", "Edwige", "Peter", "James"],
               ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]]
def sum_of_students(list):
    integer = 0
    for nbList in list:
        for nbStudent in nbList:
            integer += 1
    print("il y a ", integer ," d'étudiants")

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

abbreviate_name("boris elmuerte")


""" 5. Sum of positive """

def positive_sum(numbers):
    onlyPositive = [x for x in numbers if x > 0] or None
    sumNumbers = sum(onlyPositive)
    print(sumNumbers)
    

xx= [1,-4,7,12]

positive_sum(xx)


""" 6. Sum mixed array """
def mixed_sum(array):
    list_string = map(int, array) 
    Total = sum(list_string)
    print(Total)

mixed_sum(['5', '0', 9, 3, 2, 1, '9', 6, 7])     
