# Write your code here
arr = sorted([0, 1, 2, 4, 3, 6, 2])
print(arr)

median = 0
ele = 0
if len(arr) % 2 == 0:
    ele = int(len(arr) / 2) - 1
else:
    # print((len(arr)+1)/2)
    ele = int((len(arr) + 1) / 2) - 1
median = arr[ele]
print(median)