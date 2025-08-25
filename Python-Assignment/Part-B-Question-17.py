user_word = input("Please enter a word: ")
normalized_word = user_word.lower()
reversed_word = normalized_word[::-1]
if normalized_word == reversed_word:
    print("Palindrome")
else:
    print("Not Palindrome")

