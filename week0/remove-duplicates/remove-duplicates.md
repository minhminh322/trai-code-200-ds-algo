# Remove Duplicates Exercise

## **remove_duplicates**(arr: StaticArray) -> StaticArray:

Write a function that receives a StaticArray that is already in sorted order, either non-descending or non-ascending. The function will return a new StaticArray with all duplicate values removed. The original array must not be modified.

You may assume that the input array will contain one or more homogeneous elements in sorted order (either all numbers, or strings, or custom objects, but never a mix of these). You do not need to write checks for these conditions.

For full credit, the function must be implemented with **O(N)** complexity.

**Example #1:**

```python
test_cases = (
    [1], [1, 2], [1, 1, 2],
    [1, 20, 30, 40, 500, 500, 500],
    [5, 5, 5, 4, 4, 3, 2, 1, 1],
    [1, 1, 1, 1, 2, 2, 2, 2]
)
for case in test_cases:
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(arr)
    print(remove_duplicates(arr))
print(arr)
```

**Output:**

> STAT_ARR Size: 1 [1]
> STAT_ARR Size: 1 [1]
> STAT_ARR Size: 2 [1, 2]
> STAT_ARR Size: 2 [1, 2]
> STAT_ARR Size: 3 [1, 1, 2]
> STAT_ARR Size: 2 [1, 2]
> STAT_ARR Size: 7 [1, 20, 30, 40, 500, 500, 500]
> STAT_ARR Size: 5 [1, 20, 30, 40, 500]
> STAT_ARR Size: 9 [5, 5, 5, 4, 4, 3, 2, 1, 1]
> STAT_ARR Size: 5 [5, 4, 3, 2, 1]
> STAT_ARR Size: 8 [1, 1, 1, 1, 2, 2, 2, 2]
> STAT_ARR Size: 2 [1, 2]
> STAT_ARR Size: 8 [1, 1, 1, 1, 2, 2, 2, 2]
