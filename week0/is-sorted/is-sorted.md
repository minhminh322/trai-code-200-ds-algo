# Is Sorted Exercise

## **is_sorted**(arr: StaticArray) -> int:

Write a function that receives a StaticArray and returns an integer that describes whether the array is sorted. The method must return: - 1 if the array is sorted in strictly ascending order. - 1 if the list is sorted in strictly descending order. - 0 otherwise.

Arrays consisting of a single element are considered sorted in strictly ascending order.
You may assume that the input array will contain one or more homogeneous elements (either all numbers, or strings, or custom objects, but never a mix of these). You do not need to write checks for these conditions.

The original array must not be modified.

For full credit, the function must be implemented with **O(N)** complexity, with no additional data structures (including Static Arrays) being created.

**Example #1:**

```python
test_cases = (
[-100, -8, 0, 2, 3, 10, 20, 100],
['A', 'B', 'Z', 'a', 'z'],
['Z', 'T', 'K', 'A', '5'],
[1, 3, -10, 20, -30, 0],
[-10, 0, 0, 10, 20, 30],
[100, 90, 0, -90, -200],
['apple']
)
for case in test_cases:
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    result = is_sorted(arr)
    space = " " if result and result >= 0 else ""
    print(f”Result:{space}{result}, {arr}”)

```

**Output:**

> Result: 1, STAT_ARR Size: 8 [-100, -8, 0, 2, 3, 10, 20, 100]
> Result: 1, STAT_ARR Size: 5 ['A', 'B', 'Z', 'a', 'z']
> Result: -1, STAT_ARR Size: 5 ['Z', 'T', 'K', 'A', '5']
> Result: 0, STAT_ARR Size: 6 [1, 3, -10, 20, -30, 0]
> Result: 0, STAT_ARR Size: 6 [-10, 0, 0, 10, 20, 30]
> Result: -1, STAT_ARR Size: 5 [100, 90, 0, -90, -200]
> Result: 1, STAT_ARR Size: 1 ['apple']
