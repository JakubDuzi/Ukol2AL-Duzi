import random

# 1. 10 random hodnot
values = [random.randint(0, 100) for _ in range(10)]
print("Původní seznam:", values)

# 2. seřazení funkcí sort()
values.sort()
print("Seřazený seznam pomocí sort():", values)

# 3. znovu 10 random hodnot
values = [random.randint(0, 100) for _ in range(10)]
print("\nPůvodní seznam pro Bubble Sort:", values)

# 4. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 5. použití Bubble Sort
bubble_sort(values)
print("Seřazený seznam pomocí Bubble Sort:", values)
