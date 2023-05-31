def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    return quicksort_random(left) + [pivot] + quicksort_random(right)
