try:
    numerator = 10
    denominator = 5
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError:
    print("Index Out of Bound.")
except:
    print("Error! result is not found")
finally:
    print("This is finally block.")
