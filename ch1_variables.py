# use for comment

#variables name is case sensitive, can start with character lower upper case or even _

cars = 10
_cars = 25
CARS = 30
kind_of_cars = "ferrari"

print(cars)
print(_cars)
print(CARS)
print(kind_of_cars)

cars = 35
print(cars)

""""
multi line comment, often used as docstrings

string is immutable
number is allowing math operation
float doesn't need to defined the decimal, you can just put directly e.g. 3.14
"""
#formatting

name = "Sekar Dewi"
type_of_car = "Rolls Royce"
school = "Foundation Testing School"

print (name + " works at " + school)

#python string.format()
print ("{} works at {}".format(name, school))

