user_string = input("Please enter a string: ")
if len(user_string) > 0:
    reversed_string = user_string[::-1]
    print(f"The reversed string is: {reversed_string}")
else:
    print("You entered an empty string, which is the same when reversed.")

