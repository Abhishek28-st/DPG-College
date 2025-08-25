try:
    number = float(input("Enter a number: "))
    if number > 0:
        print(f"The number {number} is Positive.")
    elif number < 0:
        print(f"The number {number} is Negative.")
    else:
        print("The number is Zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")