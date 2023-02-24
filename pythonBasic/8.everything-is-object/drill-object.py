x = 10  # Creating the int() instance
y = 10
print(id(x), id(y))
print(x is y) 

x += 1
print(id(x), id(y))
print(x is y) 

person = ["James", "Bond", "007", "Secret agent"]
person_copy = person
print(id(person), id(person_copy))

person += ["English"]
person_copy += ["Man"]
print(id(person), id(person_copy))
print(person, person_copy)