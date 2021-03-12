'''class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created!")
    def who_am_i(self):
        print("I am a dog!")
    def bark(self):
        print("bork bork bork")

mydog = Dog()
mydog.bark()
mydog.who_am_i()
mydog.eat()
mydog.bark()
'''
'''class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"


class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)
'''

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

    def speak(self):
        return self.name+ " says woof!"

class Cat(Animal):

    def speak(self):
        return self.name+ " says meow!"

molly = Dog("Molly")
sydman = Cat("Sydman")

print(molly.speak())
print(sydman.speak())