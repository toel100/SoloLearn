""""
comparison operators return Boolean True or False: <, <=, >, >=, ==, !=
"""
print(1<1)
print(1<=1)
print(1>1)
print(1>=1)
print(1==1)
print(1!=1)

""""
control structures : if, elif, else
once the condition is met, none of the other conditions matter.
"""
name = input("what is your name?")

if name == "Sekar":
    print("Hi Sekar")

elif name == "Ivy":
    print("Hi Ivy")

else:
    print("Hi {}".format(name))

print("Thanks for entering your name, {}. Have a nice day!".format(name))

