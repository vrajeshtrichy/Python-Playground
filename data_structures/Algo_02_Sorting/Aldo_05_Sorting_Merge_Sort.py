numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print('Before Sorting: ', numbers)


def mergeSort(array):
    if len(array) == 1:
        return array

    # Split Array in into right and left
    midIndex = len(array) // 2
    left = array[:midIndex]
    right = array[midIndex:]
    # print('left', left)
    # print('right', right)
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    # print('--', left, right)
    mergedArr = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            mergedArr.append(left[leftIndex])
            leftIndex += 1
        else:
            mergedArr.append(right[rightIndex])
            rightIndex += 1
    print(left, right)
    return mergedArr + (left[leftIndex:]) + (right[rightIndex:])


answer = mergeSort(numbers)
print('After Sorting: ', answer)
