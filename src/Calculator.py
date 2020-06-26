
def addition():
    num1 = input("Enter the number :")
    num2 = input("Enter the 2nd number : ")
    num3 = num1 + num2
    print("Addition of num1 and num2: ",num3)

def subtraction():
    num1 = input("Enter the number :")
    num2 = input("Enter the 2nd number : ")
    num3 = num1 - num2
    print("Subtraction of num1 and num2: ",num3)

def multiplication():
    num1 = input("Enter the number :")
    num2 = input("Enter the 2nd number : ")
    num3 = num1 * num2
    print("Multiplication of num1 and num2: ",num3)

def division():
    num1 = input("Enter the number :")
    num2 = input("Enter the 2nd number : ")
    num3 = (num1/num2)
    print("Division of num1 and num2: ",num3)

def calculator():
    on = True
    while on:
        operation = raw_input("Enter the operation to perform + , - , * , / :")
        if operation == '+':
            addition()
        elif operation == '-':
            subtraction()
        elif operation == '*':
            multiplication()
        elif operation == '/':
            division()
        elif operation == 'q':
            on = False
            print("Closing the Calculator")
        else:
            print("entered incorrect operation")


calculator()