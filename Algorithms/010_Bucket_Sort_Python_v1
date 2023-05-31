def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        index = int(n * arr[i])
        buckets[index].append(arr[i])
    for i in range(n):
        buckets[i] = sorted(buckets[i])
    result = []
    for i in range(n):
        result.extend(buckets[i])
    return result
