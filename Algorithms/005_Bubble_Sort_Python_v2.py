def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Usage:
arr = [5, 3, 8, 4, 2]
bubble_sort(arr)
print(arr)
