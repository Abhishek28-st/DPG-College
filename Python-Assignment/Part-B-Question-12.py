user_sentence = input("Please enter a sentence: ")
length = len(user_sentence)
if length > 0:
    middle_point = length // 2
    first_half = user_sentence[:middle_point]
    second_half = user_sentence[middle_point:]
    print(f"The first half is: '{first_half}'")
    print(f"The second half is: '{second_half}'")
else:
    print("You did not enter a sentence.")
