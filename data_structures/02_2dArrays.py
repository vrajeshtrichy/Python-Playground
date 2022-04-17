arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
for r in arr:
    print(r)
maxSum = 0
for i in range(len(arr)-2):
    for j in range(len(arr[0])-2):
        sum = 0
        for ii in range(i, i+3):
            for jj in range(j, j+3):
                if (ii == i+1) and (jj == j or jj == j+2):
                    pass
                else:
                    print(arr[ii][jj])
                    sum += arr[ii][jj]
        if (i == 0 and j == 0) or (sum > maxSum):
            # This is added because in case when all the elements are negative,
            # the sum in the subset will be less than zero
            maxSum = sum
        print("=========== ", maxSum)