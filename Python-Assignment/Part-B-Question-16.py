try:
    marks = float(input("Enter your marks (0-100): "))
    if 0 <= marks <= 100:
        if marks >= 33:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Invalid input. Please enter a number between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a valid number for your marks.")

