str = input("Enter a string: ")
reversed_str = ""
for char in str:
    reversed_str = char + reversed_str
print(f"The reversed string is: {reversed_str}")