string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 > string2:
    print(f"'{string1}' is lexicographically larger.")
elif string2 > string1:
    print(f"'{string2}' is lexicographically larger.")
else:
    print("The strings are identical.")

