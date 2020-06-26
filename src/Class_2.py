class Circle():

    pi = 3.14

    def __init__(self,radius):
        self.radius = radius

    def get_circumference(self):

        print(self.pi*self.radius*2)

my_circle = Circle.pi

print(Circle.pi)

my_circle = Circle(5)

print(my_circle.radius)

my_circle.get_circumference()