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
    action, x, y = list(map(int, q))
    idx = (x ^ lastAnswer) % n
    if action == 1:
        print(q[1], idx)
        arr[idx].append(y)
        print(arr)
    elif action == 2:
        print(q[1], idx)
        temp = arr[idx]
        lastAnswer = arr[idx][y % len(temp)]
        answers.append(lastAnswer)
        print(lastAnswer)
print(answers)