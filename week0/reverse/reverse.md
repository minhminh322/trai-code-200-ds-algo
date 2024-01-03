# Reverse Exercise

## **reverse**(arr: StaticArray) -> None:

Write a function that receives a StaticArray and reverses the order of the elements in the array. The reversal must be done ‘in place’, meaning that the original input array will be modified, and you may not create another array (nor need to). You may assume that the input array will contain at least one element. You do not need to check for this condition.

For full credit, the function must be implemented with **O(N)** complexity.

**Example #1:**

```python
source = [_ for _ in range(-20, 20, 7)]
arr = StaticArray(len(source))
for i, value in enumerate(source):
    arr.set(i, value)
print(arr)
reverse(arr)
print(arr)
reverse(arr)
print(arr)
```

**Output:**

> STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15]
> STAT_ARR Size: 6 [15, 8, 1, -6, -13, -20]
> STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15]
