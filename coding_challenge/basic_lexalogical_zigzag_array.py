n = 8
a = [1, 2, 3, 4, 5, 6, 7, 8]
a.sort()
print(a)
mid = int((n + 1) / 2) - 1
print(mid)
print(a[mid], a[n - 1])
a[mid], a[n - 1] = a[n - 1], a[mid]
print(a)
st = mid + 1
ed = n - 2
while (st <= ed):
    print(a[st], a[ed])
    a[st], a[ed] = a[ed], a[st]
    print(a)
    st = st + 1
    ed = ed - 1

for i in range(n):
    if i == n - 1:
        print(a[i])
    else:
        print(a[i], end=' ')

# OUTPUT 1 2 3 8 7 6 5 4
