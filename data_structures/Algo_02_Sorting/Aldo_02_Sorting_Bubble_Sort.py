numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
print('Before Sorting: ',numbers)

def bubbleSort(array):
    pointer = len(array) - 1
    while pointer > 0:
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
        pointer -= 1
    return array


bubbleSort(numbers) # O(n^2)
# numbers will be sorted as they are passed as reference
print('After Sorting: ',numbers)
