num = int(input("Enter a number: "))
if num > 0:
    total_sum = num * (num + 1) // 2
    print(f"The sum of first {num} natural numbers is {total_sum}")
else:   
    print("Please enter a positive integer.")   
