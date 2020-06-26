
car = {"make":"bmw","model":"325i","year":"2010"}

try:
    print(car["color"])

except:
    print("No such key")

finally:
    print("Finally is executed")


