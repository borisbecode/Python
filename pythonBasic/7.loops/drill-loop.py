""" 1. Display all students in the students list in alphabetical order. """

students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "Raphaël",
    "Axel",
    "Mathieu",
    "Adrien",
]
for x in students:
    print(x) 



""" 2. Display only the names which begin with the letter "M". """

for x in students:
    if 'M' in x:
        print(x) 




""" 3. Display integers from 0 to 15 not included, using a for loop and the range() instruction. """

for i in range(1, 15):
    print(i) 





""" 4. Create a for loop that displays integers from 1 to 10 included, but use the break instruction to interrupt it at 5.  """  
for i in range(1, 10):
    print(i)
    if i == 5:
        break 





""" 5. Create a for loop that displays integers from 1 to 10 included, but use the continue to modify its execution at 5. """

for i in range(1, 11):
    print(i)
    if i > 5:
        continue
        i = i+1 
    

""" 6. Follow the instructions : """
list_of_numbers = [17, 38, 10, 25, 72]
x = sorted(list_of_numbers)
print(x)
list_of_numbers.append(12)
print(list_of_numbers)
list_of_numbers.reverse()
print(list_of_numbers)
print(list_of_numbers.index(17))
list_of_numbers.remove(38)
print(list_of_numbers)

list = []
for i in range(1, 3):
    
    list.append(list_of_numbers[i])
    if i ==2:
        print(list)
        break

list2 = []
for i in range(0, 2):
    
    list2.append(list_of_numbers[i])
    if i ==1:
        print(list2)
        break

list3 = []
for i in range(2, 5):
    
    list3.append(list_of_numbers[i])
    if i ==4:
        print(list3)
        break  

print(list_of_numbers[-1])  




""" 7. Write an algorithm that: """

whichNumber = int(input("rentre un nombre : "))
while whichNumber >= 0:
    print(whichNumber)
    whichNumber -= 1 


""" 8.The price is right !"""


from random import randint

value = randint(0, 10)
userNumber = int(input("tu dois trouver un numéro secret \n rentres un chiffre je te dirai si tu es trop haut ou trop bas \n ton chiffre : "))

while True: 
    if userNumber > value:
        userNumber= int(input("its less\n essaie encore :"))
        
        
    elif userNumber < value:
         userNumber= int(input("its more\n essaie encore :"))
         
    elif userNumber == value:
        print("you win ! ")
        break
     

""" 9. Display all students with the sentence "NAME is an alumni. " """

all_students = [
    ["David", "Justine", "Valentin", "Axel", "Redouane"],
    ["Julie", "Stéphane", "Mostapha", "Claudiu", "Son"],
]
for x in all_students:
    for b in x :
        print(b,'is a goat')




""" 10. Display all elements.  """

languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]

for x in languages:
    for b in languages[0]:
            print(b,"it's a backend language")
    for c in languages[1]:
            print(c,"it's a frontend language")
    break



