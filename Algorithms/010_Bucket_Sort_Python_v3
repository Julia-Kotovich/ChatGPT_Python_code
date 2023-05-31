def bucket_sort(arr):
    # Determine the number of buckets
    num_buckets = len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Calculate the range of each bucket
    bucket_range = (max_val - min_val) / num_buckets

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Sort each bucket using any sorting algorithm
    for bucket in buckets:
        bucket.sort()

    # Concatenate the sorted buckets
    sorted_arr = [num for bucket in buckets for num in bucket]

    return sorted_arr

# Usage:
arr = [0.42, 0.32, 0.73, 0.69, 0.55, 0.21, 0.25]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
