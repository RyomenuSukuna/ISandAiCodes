def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:# to sort in descending order, change > to < in this line
                min_idx = i

        # Swap the minimum element with the first unsorted element
        array[step], array[min_idx] = array[min_idx], array[step]

data = [2, 45, 0, 11, 9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:', data)
