# Array Range Exercise

## **sa_range**(start: int, end: int) -> StaticArray:

Write a function that receives the two integers start and end, and returns a StaticArray that contains all the consecutive integers between start and end (inclusive).

For full credit, the function must be implemented with **O(N)** complexity.

**Example #1:**

```python
cases = [(1, 3), (-1, 2), (0, 0), (0, -3), (-95, -89), (-89, -95)]
for start, end in cases:
    print(f”Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}”)
```

**Output:**

> Start: 1, End: 3, STAT_ARR Size: 3 [1, 2, 3]
> Start: -1, End: 2, STAT_ARR Size: 4 [-1, 0, 1, 2]
> Start: 0, End: 0, STAT_ARR Size: 1 [0]
> Start: 0, End: -3, STAT_ARR Size: 4 [0, -1, -2, -3]
> Start: -95, End: -89, STAT_ARR Size: 7 [-95, -94, -93, -92, -91, -90, -89]
> Start: -89, End: -95, STAT_ARR Size: 7 [-89, -90, -91, -92, -93, -94, -95]
