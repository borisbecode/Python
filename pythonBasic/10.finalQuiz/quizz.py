""" Create a variable string containing "toto" and a variable number containing the number 10. """

string = "toto"
number = 10

""" Convert string to unicode and number to float. """

numberFloat = float(number)
stringUnicode = string.encode()
print(stringUnicode)

""" Reverse the contents of the variables string and number (from line 1). """
print(string[::-1])
print(str(number)[::-1])

""" Create a list first_list containing the following integers: 1, 3, 2, 7, 4, 10, 46. """
first_list =[1,3,2,7,4,10,46]
print(first_list[:2])

""" Create a second_list that contains only the 3rd, 4th and 5th elements of first_list . """
second_list = first_list[2:-2] 
print(second_list)

third_list = first_list + second_list

""" Using the zip function, associate the values of first_list and second_list in the variable tuple_of_lists. """

turples_of_list = zip(first_list,second_list)

first_list.append(5)
print(first_list)

third_list.append(None)

""" Write a function that takes as arguments a list my_list and an integer n and returns the result of n concatenations of my_list with itself. """

def concatenate(list,n=2):
    
    print(list * n)

listy = [1,2,3,4]

concatenate(listy)

""" With a while loop, print each element of third_list up to the null element. """
index=0
while index<len(third_list[:-1]) :
    element = third_list[index]
    print(element)
    
    index += 1

""" Calculate, with a for loop, the number of even integers present in the list first_list.    """

def even(my_list):
    count = 0
    for num in my_list:
        if num % 2 == 0:
            count += 1
    print(count)
           
    return count

even(first_list)

""" Rewrite the following expression with a multi-line for loop. """

evenNumbers = []
for element in first_list:
    if element % 2 == 0:
        evenNumbers.append(element)
print(evenNumbers)        



""" Create a function that takes a string as input and returns the first single letter of the string """

def abbreviate_name(name):
    firstLetter = name[0]
    print(firstLetter)

abbreviate_name("boris")    


""" c) Dictionaries
Create a car dictionary with the following keys and values: """
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

""" Access the year value. """
print(car.get('year'))

""" Use a loop to display all the dictionary keys. """

for key in car.keys():
    print(key)


for value in car.values():
    print(value)

""" Use a loop to display all the items in the dictionary. Display also the index of each loop iteration (enumerate function). """
for index, (key, value) in enumerate(car.items()):
    print(f"{index}: {key} - {value}")


"""  create a dictionary with the given keys and values using dictionary comprehension """
dictionnaire = {f"cle_{i}": {"car"} for i in range(1, 4)}


print(dictionnaire)


""" d) Functions
Create a Fibonacci function called fibonacci (Fibonacci sequence: 0 1 1 2 3 5 8 13 ...) """


def fibonacci(n):
  

    fib_sequence = [0, 1]
    
   
    while fib_sequence[-1] < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    
    print(fib_sequence)

fibonacci(10)