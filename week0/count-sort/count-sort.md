# Count Sort Exercise

## **count_sort**(arr: StaticArray) -> StaticArray:

Use the **count sort algorithm** to write a function that receives a StaticArray and returns a new StaticArray with the same content sorted in non-ascending order. The original array must not be modified.

You may assume that the input array will contain at least one element, and that all elements will be integers in the range [-109, 109]. It is guaranteed that the difference between the maximum and minimum values in the input will be less than 1,000. You do not need to write checks for these conditions.

Implement a solution that can sort at least 5,000,000 elements in a reasonable amount of time (under a minute). Note that using a traditional sorting algorithm (even a fast sorting algorithm like **merge sort** or **shell sort**) will not pass the largest test case of 5,000,000 elements.

For full credit, the function must be implemented with **O(n+k)** time complexity, **where n is the number of elements and k is the range of values.**

Hint: The **count sort algorithm** (also known as **counting sort**) creates a sorted array by counting the number of times each value appears in the unsorted array.

A possible first step would be to find the range of numbers in the array, and use that range to create a new ‘count array’ that tabulates the number of times each element is present in the original array. The ‘count array’ will then provide you with the information you need to generate a sorted array.

Other functions in this assignment will help you determine how many different values could be in the array, as well as the range of possible values present.

**Example #1:**

```python
test_cases = (
    [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
    [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
    [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
)
for case in test_cases:
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    before = arr if len(case) < 50 else 'Started sorting large array'
    print(f”Before: {before}”)
    result = count_sort(arr)
    after = result if len(case) < 50 else 'Finished sorting large array'
    print(f”After: {after}”)
```

**Output:**

> Before: STAT_ARR Size: 5 [1, 2, 4, 3, 5]
> After : STAT_ARR Size: 5 [5, 4, 3, 2, 1]
> Before: STAT_ARR Size: 5 [5, 4, 3, 2, 1]
> After : STAT_ARR Size: 5 [5, 4, 3, 2, 1]
> Before: STAT_ARR Size: 7 [0, -5, -3, -4, -2, -1, 0]
> After : STAT_ARR Size: 7 [0, 0, -1, -2, -3, -4, -5]
> Before: STAT_ARR Size: 7 [-3, -2, -1, 0, 1, 2, 3]
> After : STAT_ARR Size: 7 [3, 2, 1, 0, -1, -2, -3]
> Before: STAT_ARR Size: 12 [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1]
> After : STAT_ARR Size: 12 [5, 5, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]
> Before: STAT_ARR Size: 4 [10100, 10721, 10320, 10998]
> After : STAT_ARR Size: 4 [10998, 10721, 10320, 10100]
> Before: STAT_ARR Size: 4 [-100320, -100450, -100999, -100001]
> After : STAT_ARR Size: 4 [-100001, -100320, -100450, -100999]

**Example #2:**

```python
array_size = 5_000_000
min_val = random.randint(-10**9, 10**9 - 998)
max_val = min_val + 998
case = [random.randint(min_val, max_val) for _ in range(array_size)]
arr = StaticArray(len(case))
for i, value in enumerate(case):
    arr[i] = value
print(f'Started sorting large array of {array_size} elements')
result = count_sort(arr)
print(f'Finished sorting large array of {array_size} elements')
```

**Output:**

> Started sorting large array of 5000000 elements
> Finished sorting large array of 5000000 elements
