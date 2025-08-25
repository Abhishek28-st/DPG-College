user_string = input("Please enter a string: ")
if len(user_string) > 0:
    if user_string[0].lower() == user_string[-1].lower():
        print("Match")
    else:
        print("No Match")
else:
    print("You entered an empty string.")