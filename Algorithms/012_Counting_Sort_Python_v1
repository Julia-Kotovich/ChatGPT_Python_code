def counting_sort(arr):
    max_val = max(arr)
    count = [0 for _ in range(max_val + 1)]
    for num in arr:
        count[num] += 1
    result = []
    for i in range(max_val + 1):
        result.extend([i] * count[i])
    return result
