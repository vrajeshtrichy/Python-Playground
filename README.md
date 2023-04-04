# python_playground

### ARRAYS

```
max(max_count, count)
```
```
sum(len(str(n)) % 2 == 0 for n in nums) 
```

#### Squares of a Sorted Array
Use Left and Right Pointers
```

```
```
def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0
```