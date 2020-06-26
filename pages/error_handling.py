def ask():
    while True:
        try:
            num = int(input('Enter a number to find Square: '))
        except ValueError:
            print('Invalid number entered - Try again')
            continue
        else:
            result = num*num
            print('Square of num is {}'.format(result))
            break
        finally:
            print('Program End')
ask()