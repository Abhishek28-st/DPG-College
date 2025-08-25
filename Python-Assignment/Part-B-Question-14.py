password = input("Please enter your password: ")
password_length = len(password)
if password_length >= 8:
    print("Strong")
else:
    print("Weak")
