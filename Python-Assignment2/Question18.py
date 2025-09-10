str = input("Enter a string  to count number of vowels and consonant: ")
vowels = 0
consonants = 0
for char in str.lower():
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")    