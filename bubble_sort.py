def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input("Enter the number of elements: "))
numbers = []

for _ in range(n):
    num = float(input("Enter a number: "))
    numbers.append(num)

print("Unsorted list:", numbers)

bubble_sort(numbers)

print("Sorted list:", numbers)
