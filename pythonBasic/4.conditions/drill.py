age = 32
age += 10
divAge = age // 7
textDiv = f" {age} divided by 7 equals {divAge}"
print(textDiv)
restDiv = age % 7
expDiv = restDiv * 3 
print(restDiv)
print(expDiv)

nombre = input("rentrez un nombre : ")
print(nombre)
str(nombre)
print(type(nombre))
integer = int(nombre)
print(type(integer))





""" 8. exercice des courses :  """
milk = 0.45
bottlesOfCider = 3.85
bagOfFlours = 0.9
butterPacket = 0.77
nutella = 1.87

listOfItems = [2*milk,3*bottlesOfCider,bagOfFlours,butterPacket,nutella]
orderPrice = sum(listOfItems)
print(orderPrice)

allowanceMoney = 20 - orderPrice

if allowanceMoney > 0 :
    message = f" you have spent {orderPrice},you have left {allowanceMoney}"
    print(message)
elif allowanceMoney == 0 :
    message = ("you are broke!")
    print(message)
else:
    message = "sorry, you dont have enough money" 
    print(message)      





""" 9. programme qui demande deux variables et donne la plus petite :  """ 

number1 = int(input("entrez un premier chiffre :"))
number2 = int(input("entrez un deuxieme chiffre :"))

if number1 > number2:
    message = f"Le plus petit chiffre est le deuxieme, a savoir {number2}"
    print(message)
else:
    print("Le plus petit nombre est le premier, a savoir : {}".format(number1)) 







""" 10. Write a script that asks you to enter 2 strings and displays the largest of the 2 strings (the one with the most characters). """

question1 = len(input("ecrivez moi deux phrases , je vous dirai laquelle contient le plus de lettre : "))    
question2 = len(input("ecrivez la deuxieme phrase : "))

if question1 > question2:
    print("la premiere phrase est plus longe")
else:
    print("la deuxieme phrase est plus longue") 







""""
11. Write a script that converts euros into dollars.

The program will start by asking the user to indicate with a character 'E' or '$' depending on the currency of the amount they are entering.
Then the program will ask you to enter the amount and display the conversion.  """  

monnaie = input("quelle est ta monnaie de départ ? \n tape E pour euro \n tape $ pour dollar \n reponse :  ")
montant = float(input("rentre le montant que tu veux convertir : "))
if(monnaie =="e" or monnaie =="E"):
    montant *= 1.06
    print(montant)
elif(monnaie =="$"): 
    montant *= 0.94
    print(montant)   




""" 12. Check if the variable name is in the studentsTuring list. (Without making a loop)

If the name is in the list, display "You are at the turing's".
Otherwise display: "You are not part of the turing's"

studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
name = "Julie" """


studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
name = "Redouane"
if(name in studentsTuring):
    print("You are at the turing's")
else:
    print("You are not part of the turing's")   







""" 13. Calculate the volume of a sphere using the formula (4π/3) x R³. The radius is 10.

Save the result in a "volume" variable.   """  


from math import pi
radius = int(input("rentrez le radius \n "))
rayon = radius / 2 
calcul = ((4*pi)/3)*rayon**3
print(f"le volume de la sphere est : {calcul}") 










