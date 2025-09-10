start = int(input("Enter a  starting number: "))
end = int(input("Enter an ending number: "))
print(f"Numbers between {start} and {end} are:")
for num in range(start + 1, end):
    print(num)

