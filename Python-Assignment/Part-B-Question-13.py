try:
    number = float(input("Enter a number: "))
    if number % 5 == 0:
        print("Buzz")
    else:
        print("Not Buzz")
except ValueError:
    print("Invalid input. Please enter a valid number.")
