user_string = input("Please enter a string: ")
if len(user_string) > 0:
    last_character = user_string[-1]
    print(f"The last character of your string is: {last_character}")
else:
    print("You entered an empty string, so there is no last character to display.")

