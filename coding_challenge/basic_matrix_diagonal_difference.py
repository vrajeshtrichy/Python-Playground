arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
n_row = len(arr)
n_col = len(arr[0])
f_diag = 0
print(arr)
for e in range(n_row):
    f_diag += arr[e][e]
print(f_diag)
i = 0
j = n_col-1
b_diag = 0
while j >= 0:
    print(arr[i][j])
    b_diag += arr[i][j]
    i += 1
    j -= 1
print(b_diag)
print(abs(f_diag-b_diag))