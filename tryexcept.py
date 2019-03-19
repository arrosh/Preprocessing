try:
    10/0
except ZeroDivisionError as err:
    print(err)
    number = int(input("Enter a number "))
     print(number)
except:
    print("Invalid Input")