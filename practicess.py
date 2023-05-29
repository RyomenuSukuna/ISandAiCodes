def selectionSort(array,size):
    for state in range(size):
        min_idx=state
        for i in range(state+1,size):
            if array[i]>array[min_idx]:
                min_idx=i
        
        array[state],array[min_idx]=array[min_idx],array[state]
        
data=[12,3,6,18,4]
size=len(data)
selectionSort(data,size)
print('Sorted array in Descending Order:',data)