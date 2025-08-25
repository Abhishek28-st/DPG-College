user_string = input("Please enter a string: ")
if len(user_string) > 0:
    every_second_char = user_string[::2]
    print(f"Every second character of your string is: {every_second_char}")
else:
    print("You entered an empty string, so there are no characters to display.")

