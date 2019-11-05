# -*- coding: utf8 -*-
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes!",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
    ]

characters = [
    "alvin et les chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "kirikou"
    ]

def get_random_quote():
    # ge a random number
    # get a quote from an array
    # show the quote in the intepreter. print()
    pass
get_random_quote()

def get_random_item_in(my_list):
    #TODO : get a random item
    item = my_list[0] #get in item from a list. For the moment, just get the first one.
    print(item)
    return "program is over" #returned value
print(get_random_item_in(quotes))

user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')    
# Show random quote
#if user_answer == "B":
# pass
#elif user_answer == "C":
  #print("C pas la bonne réponse! Et pas d'humour, je c..")
#else :
# show another quote
