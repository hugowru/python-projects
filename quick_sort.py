
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

n = int(input("Enter the number of elements: "))
numbers = []

for _ in range(n):
    num = float(input("Enter a number: "))
    numbers.append(num)

print("Unsorted list:", numbers)

sorted_numbers = quick_sort(numbers)

print("Sorted list:", sorted_numbers)
