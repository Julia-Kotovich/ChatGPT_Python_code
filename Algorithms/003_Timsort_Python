def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

def merge(left, right):
    if not left:
        return right
    
    if not right:
        return left
    
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def timsort(array):
    MIN_RUN = 32
    n = len(array)
    for i in range(0, n, MIN_RUN):
        insertion_sort(array, i, min((i + MIN_RUN - 1), n - 1))
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1]
            )
            array[start:start + len(merged_array)] = merged_array
        size *= 2
    return array
