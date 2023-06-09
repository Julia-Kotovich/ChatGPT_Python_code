def cubesort(arr):
    n = len(arr)
    max_val = max(arr)  # find the maximum value in the array
    cubes = [0] * (max_val + 1)  # create an array of zeros with size of (max_val + 1)
    sorted_arr = [0] * n  # create an empty array to hold the sorted values

    # count the occurrences of each value in the array and store them in the cubes array
    for i in range(n):
        cubes[arr[i]] += 1

    # modify the cubes array to contain the number of values <= to the current index
    for i in range(1, max_val + 1):
        cubes[i] += cubes[i - 1]

    # use the cubes array to place each value in its correct sorted position in the sorted_arr
    for i in range(n):
        sorted_arr[cubes[arr[i]] - 1] = arr[i]
        cubes[arr[i]] -= 1

    return sorted_arr
