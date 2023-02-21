age = 32
age += 10
divAge = age // 7
textDiv = f" {age} divided by 7 equals {divAge}"
print(textDiv)
restDiv = age % 7
expDiv = restDiv * 3 
print(restDiv)
print(expDiv)

""" nombre = input("rentrez un nombre : ")
print(nombre)
str(nombre)
print(type(nombre))
integer = int(nombre)
print(type(integer)) """

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

""" number1 = int(input("entrez un premier chiffre :"))
number2 = int(input("entrez un deuxieme chiffre :"))

if number1 > number2:
    message = f"Le plus petit chiffre est le deuxieme, a savoir {number2}"
    print(message)
else:
    print("Le plus petit nombre est le premier, a savoir : {}".format(number1))   """  

question1 = len(input("ecrivez moi deux phrases , je vous dirai laquelle contient le plus de lettre : "))    
question2 = len(input("ecrivez la deuxieme phrase : "))


if question1 > question2:
    print("la premiere phrase est plus longe")
else:
    print("la deuxieme phrase est plus longue")    







