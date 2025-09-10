
n = int(input("Enter the value of n: "))
count = 0
num = 2
while count < n:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    num += 1
print(f'Here is the list of firt {n} prime numbers')