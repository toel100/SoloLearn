def user_info(name, age=0, city="Tilburg"):
    ''''
    this function print name, age, city from an argument provided to the function
    '''
    print("{} is {} years old, from {}".format(name, age, city))


user_info("Sekar", 38, "Jakarta")
user_info("Ivy")
user_info(age=39, name="Elfin")

""""
*arg allows for unlimited arguments to be passed to function
**kwargs allows a function to take any number of keywords arguments
"""

def add(*args):
    print(sum(args))


add(1,2,3,4,5)

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {} with email address is {}".format(fname,lname,company,email))


application("Sekar", "Dewi", "toel100@yahoo.com", "CBA", 35000, hire_date="Oct 2009")