# Rotate Exercise

## **rotate**(arr: StaticArray, steps: int) -> StaticArray:

Write a function that receives two parameters - a StaticArray and an integer value (called _steps_). The function will create and return a new StaticArray, which contains all of the elements from the original array, but their position has shifted right or left steps number of times. The original array must not be modified.

If _steps_ is a positive integer, the elements will be rotated to the right. If _steps_ is a negative integer, they will rotate to the left. Please see the code examples below for additional details. You may assume that the input array will contain at least one element. You do not need to check for this condition.

Please note that the value of the _steps_ parameter can be very large (between -109 and 109). Your implementation must rotate an array of at least 1,000,000 elements in a reasonable amount of time (under a minute).

For full credit, the function must be implemented with **O(N)** complexity.

**Example #1:**

```python
source = [_ for _ in range(-20, 20, 7)]
arr = StaticArray(len(source))
for i, value in enumerate(source):
    arr.set(i, value)
print(arr)
for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
    space = " " if steps >= 0 else ""
    print(f”{rotate(arr, steps)} {space}{steps}”)
print(arr)
```

**Output:**

> STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15]
> STAT_ARR Size: 6 [15, -20, -13, -6, 1, 8] 1
> STAT_ARR Size: 6 [8, 15, -20, -13, -6, 1] 2
> STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15] 0
> STAT_ARR Size: 6 [-13, -6, 1, 8, 15, -20] -1
> STAT_ARR Size: 6 [-6, 1, 8, 15, -20, -13] -2
> STAT_ARR Size: 6 [-6, 1, 8, 15, -20, -13] 28
> STAT_ARR Size: 6 [8, 15, -20, -13, -6, 1] -100
> STAT_ARR Size: 6 [-6, 1, 8, 15, -20, -13] 268435456
> STAT_ARR Size: 6 [-6, 1, 8, 15, -20, -13] -2147483648
> STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15]

**Example #2:**

```python
array_size = 1_000_000
source = [random.randint(-10**9, 10**9) for _ in range(array_size)]
arr = StaticArray(len(source))
for i, value in enumerate(source):
    arr[i] = value
print(f'Started rotating large array of {array_size} elements') rotate(arr, 3**14)
rotate(arr, -3**15)
print(f'Finished rotating large array of {array_size} elements')
```

**Output:**

> Started rotating large array of 1000000 elements
> Finished rotating large array of 1000000 elements
