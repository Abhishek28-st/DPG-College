triangle = int(input("Enter the number of rows for the triangle: "))
for i in range(1, triangle + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print() 