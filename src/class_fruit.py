class Fruit:

    def __init__(self):
        print("I am a fruit")

    def nutrition(self):
        print("Nutrition of the fruit")

    def fruit_shape(self):
        print("Shape of the fruit")

class Apple(Fruit):

    def __init__(self,colour):
        self.colour = colour
        Fruit.__init__(self)
        print("I am an Apple")


    def nutrition(self):
        print("Nutrition of Apple is Good")

    def color(self):
        print("Apple is of the color {}".format(self.colour))

    def fruit_shape(self):
        print("Apple is round")



x = (input("Enter the color for the Apple : "))
print(type(x))
a = Apple(x)
print("In Child Class")
a.nutrition()
a.fruit_shape()
a.color()