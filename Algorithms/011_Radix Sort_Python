def radix_sort(arr):
    max_val = max(arr)
    num_digits = len(str(max_val))
    for digit in range(num_digits):
        buckets = [[] for _ in range(10)]
        for num in arr:
            buckets[(num // (10 ** digit)) % 10].append(num)
        arr = [num for bucket in buckets for num in bucket]
    return arr
