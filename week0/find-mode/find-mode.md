# Find Mode Exercise

## **find_mode**(arr: StaticArray) -> tuple[object, int]:

Write a function that receives a StaticArray that is sorted in either non-descending or non-ascending order. The function will return the mode (the most-occurring element) of the array and its frequency (how many times it appears).

If there is more than one element that has the highest frequency, select the one that occurs first in the array.

You may assume that the input array will contain one or more homogeneous elements (either all numbers, or strings, or custom objects, but never a mix of these). You do not need to write checks for these conditions.

For full credit, the function must be implemented with **O(N)** complexity, with no additional data structures (including Static Arrays) being created.

**Example #1:**

```python
test_cases = (
[1, 20, 30, 40, 500, 500, 500],
[2, 2, 2, 2, 1, 1, 1, 1],
["zebra", "sloth", "otter", "otter", "moose", "koala"], ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
)
for case in test_cases:
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value

    result = find_mode(arr)
    if result:
        print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
    else:
        print(“find_mode() not yet implemented”)
```

**Output:**

> STAT_ARR Size: 7 [1, 20, 30, 40, 500, 500, 500]
> Mode: 500, Frequency: 3
>
> STAT_ARR Size: 8 [2, 2, 2, 2, 1, 1, 1, 1]
> Mode: 2, Frequency: 4
>
> STAT_ARR Size: 6 ['zebra', 'sloth', 'otter', 'otter', 'moose', 'koala']
> Mode: otter, Frequency: 2
>
> STAT_ARR Size: 6 ['Albania', 'Belgium', 'Chile', 'Denmark', 'Egypt', 'Fiji']
> Mode: Albania, Frequency: 1
