# Min Max Exercise

## **min_max**(arr: StaticArray) -> tuple[int, int]:

Write a function that receives a one-dimensional array of integers and returns a Python tuple with two values - the minimum and maximum values of the input array.

The content of the input array must not be changed. You may assume that the input array will contain only integers, and will have at least one element. You do not need to check for these conditions.

For full credit, the function must be implemented with **O(N)** complexity.

**Example #1:**

```python
arr = StaticArray(5)
for i, value in enumerate([7, 8, 6, -5, 4]):
    arr[i] = value
print(arr)
result = min_max(arr)
if result:
    print(f”Min: {result[0]: 3}, Max: {result[1]}”)
else:
    print(“min_max() not yet implemented”)
```

**Output:**

> STAT_ARR Size: 5 [7, 8, 6, -5, 4]
> Min: -5, Max: 8

**Example #2:**

```python
arr = StaticArray(1)
arr[0] = 100
print(arr)
result = min_max(arr)
if result:
    print(f”Min: {result[0]}, Max: {result[1]}”)
else:
    print(“min_max() not yet implemented”)
```

**Output:**

> STAT_ARR Size: 1 [100]
> Min: 100, Max: 100![ref1]

**Example #3:**

```python
print('\n# min\_max example 3')
test_cases = (
    [3, 3, 3],
    [-10, -30, -5, 0, -10],
    [25, 50, 0, 10],
)

for case in test_cases:
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f”Min: {result[0]: 3}, Max: {result[1]}”)
    else:
        print(“min_max() not yet implemented”)
```

**Output:**

> STAT_ARR Size: 3 [3, 3, 3]
> Min: 3, Max: 3
> STAT_ARR Size: 5 [-10, -30, -5, 0, -10] Min: -30, Max: 0
> STAT_ARR Size: 4 [25, 50, 0, 10]
> Min: 0, Max: 50
