user_string = input("Please enter a string: ")
length = len(user_string)
if length == 0:
    print("You entered an empty string, so there are no middle characters.")
else:
    middle_index = length // 2
    if length % 2 == 0:
        middle_characters = user_string[middle_index - 1:middle_index + 1]
        print(f"The middle two characters are: '{middle_characters}'")
    else:
        middle_character = user_string[middle_index]
        print(f"The middle character is: '{middle_character}'")
