def mergeSort_version1(arr1, arr2):
    mergedArr = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] <= arr2[0]:
            mergedArr.append(arr1[0])
            arr1.pop(0)
        elif arr2[0] < arr1[0]:
            mergedArr.append(arr2[0])
            arr2.pop(0)
    mergedArr.extend(arr1)
    mergedArr.extend(arr2)
    return mergedArr


def mergeSort_version2(arr1, arr2):
    mergedArr = []
    while len(arr1) > 0 or len(arr2) > 0:
        if len(arr2) == 0 or arr1[0] <= arr2[0]:
            mergedArr.append(arr1[0])
            arr1.pop(0)
        elif len(arr1) == 0 or arr2[0] < arr1[0]:
            mergedArr.append(arr2[0])
            arr2.pop(0)
    return mergedArr


array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]
print(mergeSort_version2(array1, array2))
