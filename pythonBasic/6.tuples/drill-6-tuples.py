my_list = ["a", "b", "c", "d"]

print(my_list[:2])

print(my_list[::-1])

my_list.append("Add Text")
print(my_list)

heroes = {}
heroes["Batman"] = "Bruce Wayne"
heroes["Superman"] = "Clark Kent"
print(heroes)



""" 1. Choose 5 words from the English language and create dictionaries that associates each of these words with its French translation. """
Translator = {}
Translator["hello"]="bonjour"
Translator["cheese"]="fromage"
Translator["shoes"]="chaussures"
Translator["stairs"]="escalier"
Translator["hand"]="main"
Translator["grass"]="herbe"

""" 3. How would you cut the following string at each space and put it in a list? """

sentence = "I am the master of the world"
phrase_to_list = sentence.split()
print(phrase_to_list)




""" 4. Transform this string "The_universal_number_is_42" by removing the underscores: "The universal number is 42" """

universal_number = "The_universal_number_is_42"
realSentence = universal_number.replace("_"," ")
print(realSentence)





""" 5. Display only values of this dictionary. """

heroes = {"Superman": "Clark Kent", "Batman": "Bruce Wayne", "Spiderman": "Tony Parker"}
print(heroes.values())





""" 6. Display only keys of this dictionary. """

heroes = {"Superman": "Clark Kent", "Batman": "Bruce Wayne", "Spiderman": "Tony Parker"}
print(heroes.keys())






""" 7. Replace the value of "Spiderman" by "Peter Parker". """

heroes = {"Superman": "Clark Kent", "Batman": "Bruce Wayne", "Spiderman": "Tony Parker"}
heroes["Spiderman"] = "Peter Parker"
print(heroes)


""" 8. Create a dictionary to build the price base of the products corresponding to the following table. """


products ={}
products["Laser sword"]= 229
products["Mitendo DX"]= 127
products["Linux cushion"]= 74.50
products["Goldorak briefs"]= 29.90
products["Nextpresso station"]= 184.60

print(products)

""" 9. Calculate the total price of the items of the dictionary. """
totalPrice = sum(products.values())
print(totalPrice)


""" 10. Remove one of the articles from the dictionary. """
del products["Laser sword"]
print(products)







