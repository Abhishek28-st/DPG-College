user_name = input("Please enter your name: ")
if len(user_name) > 0:
    uppercase_name = user_name.upper()
    print(f"Your name in uppercase is: {uppercase_name}")
    lowercase_name = user_name.lower()
    print(f"Your name in lowercase is: {lowercase_name}")
else:
    print("You did not enter a name.")

