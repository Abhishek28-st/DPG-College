def simple_sort(number):
    n = len(number)
    for i in range(n):
        for j in range(0, n-i-1):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
    return number
num = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List is:", num)
sorted_list = simple_sort(num)
print("Sorted array is:", sorted_list) 