def addition():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a+b)

def user_info(name, age , city):

    print ('{} is {} years old , from {}'.format(name,age,city))


def conditions():
    nam1 = raw_input("Enter your name here :")
    if nam1 == "ARUN":
        print("Awesome! Name is {}".format(nam1))
    else:
        print("I dont know you")

conditions()