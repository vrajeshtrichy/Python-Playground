n = 2
queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
lastAnswer = 0
answers = []
for r in queries:
    print(r)
arr = []
for i in range(n):
    arr.append([])
print(arr)
for q in queries:
    idx = (q[1] ^ lastAnswer) % n
    if q[0] == 1:
        print(q[1], idx)
        arr[idx].append(q[2])
        print(arr)
    elif q[0] == 2:
        print(q[1], idx)
        temp = arr[idx]
        lastAnswer = arr[idx][q[2] % len(temp)]
        answers.append(lastAnswer)
        print(lastAnswer)
print(answers)