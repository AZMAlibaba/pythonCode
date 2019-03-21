while True:
    try:
        x = int(input("Input first number:"))
        y = int(input("Input second number:"))
        print(x/y)
    except Exception as e:
        print(e)
    else:
        break