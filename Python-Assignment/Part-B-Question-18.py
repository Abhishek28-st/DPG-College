try:
    age = int(input("Please enter your age: "))
    if age >= 0:
        if age < 13:
            print("Child")
        elif 13 <= age <= 19:
            print("Teenager")
        else:
            print("Adult")
    else:
        print("Invalid input. Age cannot be negative.")

except ValueError:
    print("Invalid input. Please enter a valid whole number for your age.")
