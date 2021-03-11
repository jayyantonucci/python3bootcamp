mylist = [1,2,3]
myset = set()

type(myset) #set
type(mylist) #list

class Sample():
    pass

my_sample = Sample()
type(my_sample) #__main__.Sample

class Dog():
    def __init__(self, breed, name, spots):
        #attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots =  spots #boolean



my_dog = Dog(breed='Husky', name='Molly', spots=False)

type(my_dog)

my_dog.breed
my_dog.name
my_dog.spots