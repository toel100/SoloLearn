""""
class features
inheritance - allow us to borrow from one class and use elements of that class to create another class
multiple inheritance - which allows a class to inherit attributes from multiple classes.

instance variables - those variables are specific to any Objects that are created by the class

__init__ method, which allows every instance of a class to be created with specific parameters
self - variable an instance of a class, and specifically it references the instance of the class that has been created.
"""
class Person:
    def __init__(self, firstname, lastname, health, status):
        """" initialize attributes to be used in/available for all class methods in this class,
            and for class Objects created by this class
        """
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status


    def introduce(self):
        """"all people introduce themselves"""
        print("Hi, I'm {} {}".format(self.firstname, self.lastname))


    def status_change(self):
        """print message based on health score"""
        if self.health == 100:
            print("{} is totally healty".format(self.firstname))

        elif self.health >= 76:
            print("{} is a little tired today".format(self.firstname))

        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))

        elif self.health >= 40:
            print("{} goes to doctor".format(self.firstname))

        else:
            print("{} is unconcious.".format(self.firstname))

Maria = Person("Maria", "Kope", 95, status=True)
Rey = Person("Rey", "Munisati", 70, status=True)
Nico = Person("Nico", "Napitupulu",50, status=False)

print("Is {} my friend? {}".format(Maria.firstname, Maria.status))
print("Is {} my friend? {}".format(Rey.firstname, Rey.status))
print("Is {} my friend? {}".format(Nico.firstname, Nico.status))

Maria.introduce()
Maria.status_change()

Rey.introduce()
Rey.status_change()

Nico.introduce()
Nico.status_change()

#inheritance example
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    #sample of polymorphism, override introduce in parent class Person
    def introduce(self):
        print("I am {}. You are my mortal Enemy".format(self.firstname))

    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -= 5
        print("{} health now is {}".format(other.firstname, other.health))

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!!".format(other.firstname))
        if other.status == True:
            other.status = False

Andhika = Enemy("rock","Andhika", "Prasetya", 77, False)
Andhika.introduce()
Andhika.hurt(Maria)
Andhika.insult(Maria)
Andhika.insult(Rey)
Andhika.steal(Rey)

#error condition due to Rey is not define as Enemy
Rey.insult(Andhika)

