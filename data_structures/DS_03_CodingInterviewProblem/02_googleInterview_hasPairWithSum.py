def hasPairWithSum_Naive(arr, sum):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == sum:
                return True
    return False


def hasPairWithSum(arr, sum):
    compliments = set()
    for e in arr:
        if e in compliments:
            return True
        compliments.add(sum - e)
    return False


print(hasPairWithSum_Naive([1, 2, 3, 4, 5], 10))
print(hasPairWithSum([1, 2, 3, 4, 5], 10))
