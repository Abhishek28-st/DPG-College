user_string = input("Please enter a string: ")
if len(user_string) >= 3:
    first_three_chars = user_string[:3]
    print(f"The first three characters of your string are: {first_three_chars}")
else:
    print("Your string is shorter than 3 characters, so I can't display the first three.")

