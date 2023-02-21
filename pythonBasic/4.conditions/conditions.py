

age = 23
if age >= 18:
    print("You're an adult!")


age = 17
if age >= 18:
    print("You're an adult!")
elif age <= 17:
    print("come later, you're too young")

name = "admins"
if name =="admin":
    print("welcome admin")
elif name =="boris":
    print("welcome boss")
else:
    print("you're not the admin , go back away or i call the police")     

student1 = "ludo"
student2 = "arnaud"
if student1 =="ludo" and student2 =="arnaud":
    print("welcome coach")
else:    
    print("you are not a coach?")    

entername = "Valérian"
coach = ["Valérian", "Ludovic"]
if entername in coach:
    print("Your are Coach!")
else:
    print("You are not coach")   

numbers= [2,3,4]
numbers2=[2,3,4]
print(numbers == numbers2)
print (numbers is numbers2)    

x= 27
y = 27
id(x)
id(y)
print(x is y)
