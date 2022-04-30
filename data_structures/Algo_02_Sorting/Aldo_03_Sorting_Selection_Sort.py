
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print('Before Sorting: ',numbers)

def selectionSort(array):
    pointer = 0
    while pointer < len(array):
        smallestElePos = pointer
        # print(pointer, array[smallestElePos])
        for i in range(pointer, len(array)):
            # print('--',pointer, array[smallestElePos], array[i])
            if array[i] < array[smallestElePos]:
                smallestElePos = i
        # SWAP the pointer element with the smallest element
        temp = array[pointer]
        array[pointer] = array[smallestElePos]
        array[smallestElePos] = temp
        # print('sorted ele', array[pointer])
        pointer += 1
    return array


selectionSort(numbers) # O(n^2)
print('After Sorting: ',numbers)