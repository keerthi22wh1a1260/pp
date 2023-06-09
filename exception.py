try:
    s=[1,2,3,4]
    for i in range(0,3):
        print(d[2])
except ZeroDivisionError:
    print("Error: denominator cannot be zero")
except IndexError:
    print("Error: Out of given Index")
except SyntaxError:
    print("Error: check the Syntax")
except NameError:
    print("Error: check the name")

