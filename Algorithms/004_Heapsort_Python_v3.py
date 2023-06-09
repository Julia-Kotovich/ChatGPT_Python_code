def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr):
    n = len(arr)

    # Heapify non-leaf nodes in reverse order
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapsort(arr):
    build_heap(arr)

    # Extract elements from the heap in descending order
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the root with the last element
        heapify(arr, i, 0)  # Restore heap property for the reduced heap

# Usage:
arr = [5, 3, 8, 4, 2]
heapsort(arr)
print(arr)
