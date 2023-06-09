def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap

        gap //= 2

# Usage:
arr = [5, 3, 8, 4, 2]
shell_sort(arr)
print(arr)
