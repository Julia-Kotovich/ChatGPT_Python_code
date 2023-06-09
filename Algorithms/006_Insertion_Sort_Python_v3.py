def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

# Usage:
arr = [5, 3, 8, 4, 2]
insertion_sort(arr)
print(arr)
