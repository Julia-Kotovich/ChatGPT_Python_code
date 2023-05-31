def cubesort(arr):
    n = len(arr)
    gap = n

    while gap > 1:
        gap = (gap * 10) // 13

        if gap < 1:
            gap = 1

        for i in range(n - gap):
            if arr[i + gap] < arr[i]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False

# Usage:
arr = [4, 2, 7, 1, 5, 3]
cubesort(arr)
print(arr)
