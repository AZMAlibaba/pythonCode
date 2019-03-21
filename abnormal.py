'''
异常处理机制
try
except
'''
try:
    x=int(input("Input variable x's value:"))
    y=int(input("Input variable y's value:"))
    print("X/Y={}".format(x/y))
except ZeroDivisionError:
    print("The second number can not be zero!")