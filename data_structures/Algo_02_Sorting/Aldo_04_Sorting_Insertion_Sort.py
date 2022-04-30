numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
print('Before Sorting: ',numbers)

def insertionSort(array):
    for pointer in range(1, len(array)):
        # print('pointer', pointer)
        # print('--',array[pointer], array[pointer-1])
        for i in range(0, pointer):
            if array[pointer] < array[i]:
                # temp = array[pointer]
                # del array[pointer]
                temp = array.pop(pointer)
                array.insert(i, temp)
                print(temp,'Inserted', array)
    return array


insertionSort(numbers) # O(n^2)
print('After Sorting: ',numbers)
