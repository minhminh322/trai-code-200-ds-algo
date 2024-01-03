# Fizz Buzz Exercise

## **fizz_buzz**(arr: StaticArray) -> StaticArray:

Write a function that receives a StaticArray of integers and returns a new StaticArray object with the content of the original array, modified as follows:

1. If the number in the original array is divisible by 3, the corresponding element in the new array will be the string ‘fizz’.
2. If the number in the original array is divisible by 5, the corresponding element in the new array will be the string ‘buzz’.
3. If the number in the original array is both a multiple of 3 and a multiple of 5, the corresponding element in the new array will be the string ‘fizzbuzz’.
4. In all other cases, the element in the new array will have the same value as in the original array.

The content of the input array must not be changed. You may assume that the input array will contain only integers, and will have at least one element. You do not need to check for these conditions.

For full credit, the function must be implemented with **O(N)** complexity.

**Example #1:**

```python
source = [_ for _ in range(-5, 20, 4)]
arr = StaticArray(len(source))
for i, value in enumerate(source):
    arr[i] = value
print(fizz_buzz(arr))
print(arr)
```

**Output:**

> STAT_ARR Size: 7 ['buzz', -1, 'fizz', 7, 11, 'fizzbuzz', 19]
>
> STAT_ARR Size: 7 [-5, -1, 3, 7, 11, 15, 19]
