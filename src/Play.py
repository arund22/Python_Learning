
a = "This is my house"

b = a.split()



sub = a[::-1]

print(b)

a = ["honda","benz","tata","kia","kia"]



b = a[::-1]

print(b)

print('#'*20)

a.sort(reverse=True)

print(a)

print(a.count(a))

print('*'*20)

d={"key1": [1, 2, 3], "key2": [4, 5, 6], "key3": [7, 8, 9]}

print(d["key1"][2])

t=(10, 20 , 30)

print(t.index(20))

print('&^'*20)

def sum(num1,num2):
    """
    Get Sum of two numbers
    :param num1:
    :param num2:
    :return:
    """

    num1+=num2
    return num1

print(sum(9,3))

print('&'*20)

def is_metro(city):
    l = ["sfo","nyc","sjc"]

    if city.lower() in l:

        return True

    else:

        return False

city = str(input("Input the city name: "))
print(is_metro(city))


