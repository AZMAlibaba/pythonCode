try:
    x=float(input("Please input first number:"))
    y=float(input("Please input second number:"))
    print("x/y 's value is {}".format(x/y))
except ZeroDivisionError:
    print("Second number can not be zero!")
except TypeError:
    print("That wasn't a number was it ?")

