class Dog():

    def __init__(self,breed,name):
        self.breed = breed
        self.name=name

    def bark(self):
        print("Woof my name is {}".format(self.name))

my_dog = Dog('Lab','Aria')
print(my_dog.name)
my_dog.bark()