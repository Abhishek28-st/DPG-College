num1 = int(input("Enter a number: ") )
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))
if (num1 > num2) and (num2 > num3):
    print(f"The Second largest number is {num2}")
elif (num1 > num3) and (num3 > num2):
    print(f"The Second largest number is {num3}")
elif (num2 > num1) and (num1 > num3):
    print(f"The Second largest number is {num1}")
elif (num2 > num3) and (num3 > num1):   
    print(f"The Second largest number is {num3}")
elif (num3 > num1) and (num1 > num2):
    print(f"The Second largest number is {num1}")
else:
    print(f"The Second largest number is {num2}")
    