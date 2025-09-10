str = input("Enter a string: ")
words = str.split()
longest_word = max(words, key=len)
print(f"The longest word in the string is: {longest_word}")   