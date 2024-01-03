# Sorted Squares Exercise

## **sorted_squares**(arr: StaticArray) -> StaticArray:

Write a function that receives a StaticArray where the elements are in sorted order, and returns a new StaticArray with squares of the values from the original array, sorted in non-descending order. The original array must not be modified.

You may assume that the input array will have at least one element, will contain only integers in the range [-10^9, 10^9], and that elements of the input array are already in non-descending order. You do not need to write checks for these conditions.

Implement a FAST solution that can process at least 5,000,000 elements in a reasonable amount of time (under a minute).

Note that using a traditional sorting algorithm (even a fast sorting algorithm like merge sort or shell sort) will not pass the largest test case of 5,000,000 elements. Also, a solution using count_sort() as a helper method will also not work here, due to the wide range of values in the input array.

For full credit, the function must be implemented with **O(N)** complexity.

**Example #1:**

```python
test_cases = (
    [1, 2, 3, 4, 5],
    [-5, -4, -3, -2, -1, 0],
    [-3, -2, -2, 0, 1, 2, 3],
)
for case in test_cases:
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(arr)
    result = sorted_squares(arr)
    print(result)
```

**Output:**

> STAT_ARR Size: 5 [1, 2, 3, 4, 5]
> STAT_ARR Size: 5 [1, 4, 9, 16, 25]
> STAT_ARR Size: 6 [-5, -4, -3, -2, -1, 0]
> STAT_ARR Size: 6 [0, 1, 4, 9, 16, 25]
> STAT_ARR Size: 7 [-3, -2, -2, 0, 1, 2, 3]
> STAT_ARR Size: 7 [0, 1, 4, 4, 4, 9, 9]

**Example #2:**

```python
array_size = 5_000_000
case = [random.randint(-10**9, 10**9) for _ in range(array_size)]
arr = StaticArray(len(case))
for i, value in enumerate(sorted(case)):
    arr[i] = value
print(f'Started sorting large array of {array_size} elements')
result = sorted_squares(arr)
print(f'Finished sorting large array of {array_size} elements')
```

**Output:**

> Started sorting large array of 5000000 elements
> Finished sorting large array of 5000000 elements
