def counting_sort(arr):
    # Find the maximum value in the array
    max_value = max(arr)

    # Create a count array to store the frequency of each element
    count = [0] * (max_value + 1)

    # Calculate the frequency of each element
    for num in arr:
        count[num] += 1

    # Calculate the cumulative sum of the count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create a sorted array to store the sorted elements
    sorted_arr = [0] * len(arr)

    # Place the elements in the sorted array based on their counts
    for num in reversed(arr):
        index = count[num] - 1
        sorted_arr[index] = num
        count[num] -= 1

    return sorted_arr

# Usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)
