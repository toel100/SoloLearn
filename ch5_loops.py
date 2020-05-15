""""
A loop is a useful construct for when you'd like to repeat the same actions any number of times.
loops
    for
    while
loop control
    break - end the loop, go to the next statement outside the loop
    continue - skips current part of the loop, moves to the next part of the loop
    pass - skips any part of the loop where "pass" appears, best used for testing code
"""

#A for loop is useful when you'd like to iterate over each item in a list
fruits = ["apple", "orange", "banana", "kiwi", "grapes"]

for fruit in fruits:
    print("would you like an {}?".format(fruit))

for number in range(1,11):
    if number == 7:
        print("We are skipping 7")
        continue
    print("Number {}.".format(number))

for number in range(1,11):
    if number == 3:
        pass
    else:
        print("Number {}.".format(number))

#A while loop will run any time a condition remains true.
temp = 37

while temp> 32:
    print("the water is not frozen at {}".format(temp))
    temp -= 1
    if temp == 34:
        break
print("Water become ice at 32 degree Fahrenheit")


