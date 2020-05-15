""""
Dictionaries are a type of Python data collection that stores the data in key/value pairs.
keys are generally made of Strings, integers, or tuples, and need to be both unique and immutable
values can be set to any data type and any number of key/value pairs can be contained in a dictionary.
can make an empty dictionary by assigning a dictionary name with nothing in the curly braces {}
Dictionaries are mutable and can be changed using the Python dictionary methods.
order of a dictionary can be maintained.
Dictionaries are created with curly braces and each key is separated from each value by a colon. :
Each key/value pair is separated from each other key/value pair with a comma. ,
"""
years = {"Layla":1974, "Ackeem":1997, "Haleh":1982 }

""""
method
get -  return the value of one of the keys in the dictionary
items - takes the name of the dictionary and outputs a view of the key/value pairs.
keys - returns a view of all of the keys in the dictionary.
popitem - allows us to remove the last item in a dictionary

setdefault - allows us to see what the value is of a key that is in the dictionary, 
but more importantly, allows us to set a default value when a key is not in the dictionary 
and to add that value to the dictionary

update - to update the first dictionary with another dictionary

"""
print(years.get("Leah"))
print(years.get("Layla"))


print(years.items())

print(years.keys())

print(years.popitem())
print(years)

print("set default")
print(years.setdefault("Layla"))
print(years)
print(years.setdefault("Komang",2000))
print(years)

#we can update and add new items at the same time with the update method.
new_years = {"Koka":56, "Kiki": 67}
years.update(new_years)
print(years)

new_years = {"Koka":70, "Kiki": 71}
years.update(new_years)
print(years)

#add items directly to the update method in order to use it.
#able to update without having to make a second dictionary
years.update(Koka = 90, Kiki = 91)
print(years)