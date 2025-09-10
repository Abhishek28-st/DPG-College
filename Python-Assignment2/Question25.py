from collections import Counter
str = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequencies = Counter(str)
print(f"Original list: {str}")
print(f"Frequencies of each element: {frequencies['apple']}")
