#Rayyan Rahman ID: 1893113

# Global variable
num_calls = 0

# Partitioning algorithm
def partition(user_ids, i, k):
    # Choose middle element as pivot
    pivot_index = (i + k) // 2
    pivot_value = user_ids[pivot_index]

    # Initialize index variables
    l = i
    h = k

    # Loop until indices cross
    while l <= h:
        # Find element on left side to swap
        while user_ids[l] < pivot_value:
            l += 1

        # Find element on right side to swap
        while user_ids[h] > pivot_value:
            h -= 1

        # Swap elements if necessary
        if l <= h:
            user_ids[l], user_ids[h] = user_ids[h], user_ids[l]
            l += 1
            h -= 1

    # Return index of pivot element
    return l


# Quicksort algorithm
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i >= k:
        return

    # Partition the array
    index = partition(user_ids, i, k)

    # Recursively sort the left and right partitions
    quicksort(user_ids, i, index - 1)
    quicksort(user_ids, index, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
