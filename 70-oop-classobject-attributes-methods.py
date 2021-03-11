class Dog():

    #class object attribute
    #same for any instance of a class

    species = 'mammal'

    def __init__(self, breed, name):
        #attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = breed
        self.name = name

    #operations/actions ---> methods
    def bark(self,number):
        print("Woof! My name is {} and I am a {}. My number is {}".format(self.name,self.breed,number))

my_dog = Dog('Sheppard', 'Molly')
number = 4

my_dog.species
my_dog.breed
my_dog.name

my_dog.bark(number)


class Circle():

    #class object attribute

    pi = 3.14

    def __init__(self,radius=1):

        self.radius = radius
        self.area = radius*radius*self.pi

    #method

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30) #overwrites default value of 1

my_circle.pi
my_circle.radius
my_circle.get_circumference()
my_circle.area