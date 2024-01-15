# Advanced Operations

## **slice**(self, start_index: int, size: int) -> object:

This method returns a new DynamicArray object that contains the requested number of elements from the original array, starting with the element located at the requested start index. If the array contains N elements, a valid start_index is in range [0, N - 1] inclusive. A valid size is a non-negative integer.
If the provided start index or size is invalid, or if there are not enough elements between the start index and the end of the array to make the slice of the requested size, **this method must raise a custom “DynamicArrayException”.**

**Example #1:**

```python
da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
da_slice = da.slice(1, 3)
print(da, da_slice, sep="\n")
da_slice.remove_at_index(0)
print(da, da_slice, sep="\n")
```

**Output:**

> DYN_ARR Size/Cap: 9/16 [1, 2, 3, 4, 5, 6, 7, 8, 9]
> DYN_ARR Size/Cap: 3/4 [2, 3, 4]
> DYN_ARR Size/Cap: 9/16 [1, 2, 3, 4, 5, 6, 7, 8, 9]
> DYN_ARR Size/Cap: 2/4 [3, 4]

**Example #2:**

```python
da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
print("SOURCE:", da)
slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
for i, cnt in slices:
    print("Slice", i, "/", cnt, end="")
    try:
        print(" --- OK: ", da.slice(i, cnt))
    except:
        print(" --- exception occurred.")
```

**Output:**

> SOURCE: DYN_ARR Size/Cap: 7/8 [10, 11, 12, 13, 14, 15, 16]
> Slice 0 / 7 --- OK: DYN_ARR Size/Cap: 7/8 [10, 11, 12, 13, 14, 15, 16]
> Slice -1 / 7 --- exception occurred.
> Slice 0 / 8 --- exception occurred.
> Slice 2 / 3 --- OK: DYN_ARR Size/Cap: 3/4 [12, 13, 14]
> Slice 5 / 0 --- OK: DYN_ARR Size/Cap: 0/4 []
> Slice 5 / 3 --- exception occurred.
> Slice 6 / 1 --- OK: DYN_ARR Size/Cap: 1/4 [16]
> Slice 6 / -1 --- exception occurred.

## **merge**(self, second_da: object) -> None:

This method takes another DynamicArray object as a parameter, and appends all elements from this array onto the current one, in the same order in which they are stored in the input array.

**Example #1:**

```python
da = DynamicArray([1, 2, 3, 4, 5])
da2 = DynamicArray([10, 11, 12, 13])
print(da)
da.merge(da2)
print(da)
```

**Output:**

> DYN_ARR Size/Cap: 5/8 [1, 2, 3, 4, 5]
> DYN_ARR Size/Cap: 9/16 [1, 2, 3, 4, 5, 10, 11, 12, 13]

**Example #2:**

```python
da = DynamicArray([1, 2, 3])
da2 = DynamicArray()
da3 = DynamicArray()
da.merge(da2)
print(da)
da2.merge(da3)
print(da2)
da3.merge(da)
print(da3)
```

**Output:**

> DYN_ARR Size/Cap: 3/4 [1, 2, 3]
> DYN_ARR Size/Cap: 0/4 []
> DYN_ARR Size/Cap: 3/4 [1, 2, 3]

## **map**(self, map_func) ->object:

This method creates a new dynamic array where the value of each element is derived by
applying a given _map_func_ to the corresponding value from the original array.

This method works similarly to the Python _map()_ function. For a review on how Python’s map() works, here is some suggested reading:

- https://docs.python.org/3/library/functions.html#map
- https://www.geeksforgeeks.org/python-map-function/

**Example #1:**

```python
da = DynamicArray([1, 5, 10, 15, 20, 25])
print(da)
print(da.map(lambda x: (x ** 2)))
```

**Output:**

> DYN_ARR Size/Cap: 6/8 [1, 5, 10, 15, 20, 25]
> DYN_ARR Size/Cap: 6/8 [1, 25, 100, 225, 400, 625]

**Example #2:**

```python
def double(value):
    return value * 2
def square(value):
    return value ** 2
def cube(value):
    return value ** 3
def plus_one(value):
    return value + 1

da = DynamicArray([plus_one, double, square, cube])
for value in [1, 10, 20]:
    print(da.map(lambda x: x(value)))

```

**Output:**

> DYN_ARR Size/Cap: 4/4 [2, 2, 1, 1]
> DYN_ARR Size/Cap: 4/4 [11, 20, 100, 1000]
> DYN_ARR Size/Cap: 4/4 [21, 40, 400, 8000]

## **filter**(self, filter_func) ->object:

This method creates a new dynamic array populated only with those elements from the
original array for which _filter_func_ returns True.

This method works similarly to the Python _filter()_ function. For a review on how Python’s filter() works, here is some suggested reading:

- https://docs.python.org/3/library/functions.html#filter
- https://www.geeksforgeeks.org/filter-in-python/

**Example #1:**

```python
def filter_a(e):
    return e > 10

da = DynamicArray([1, 5, 10, 15, 20, 25])
print(da)
result = da.filter(filter_a)
print(result)
print(da.filter(lambda x: (10 <= x <= 20)))

```

**Output:**

> DYN_ARR Size/Cap: 6/8 [1, 5, 10, 15, 20, 25]
> DYN_ARR Size/Cap: 3/4 [15, 20, 25]
> DYN_ARR Size/Cap: 3/4 [10, 15, 20]

**Example #2:**

```python
def is_long_word(word, length):
    return len(word) > length
da = DynamicArray("This is a sentence with some long words".split())
print(da)
for length in [3, 4, 7]:
    print(da.filter(lambda word: is_long_word(word, length)))

```

**Output:**

> DYN_ARR Size/Cap: 8/8 [This, is, a, sentence, with, some, long, words]
> DYN_ARR Size/Cap: 6/8 [This, sentence, with, some, long, words]
> DYN_ARR Size/Cap: 2/4 [sentence, words]
> DYN_ARR Size/Cap: 1/4 [sentence]

## **reduce**(self, reduce_func, initializer=None) ->object:

This method sequentially applies the _reduce_func_ to all elements of the dynamic array and returns the resulting value. It takes an optional initializer parameter. If this parameter is not provided, the first value in the array is used as the initializer. If the dynamic array is empty, the method returns the value of the initializer (or None, if one was not provided).

This method works similarly to the Python _reduce()_ function. For a review on how Python’s reduce() works, here is some suggested reading:

- https://www.geeksforgeeks.org/reduce-in-python/

**Example #1:**

```python
values = [100, 5, 10, 15, 20, 25]
da = DynamicArray(values)
print(da)
print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
print(da.reduce(lambda x, y: (x + y ** 2), -1))

```

**Output:**

> DYN_ARR Size/Cap: 6/8 [100, 5, 10, 15, 20, 25]
> 714
> 11374
> Explanation:
> 45 = (100 // 5) + 5^2
> 109 = (45 // 5) + 10^2
> 246 = (109 // 5) + 15^2
> 449 = (246 // 5) + 20^2
> 714 = (449 // 5) + 25^2
>
> # -1 is the initializer
>
> 11374 = -1 + 100^2+ 5^2 + 10^2 + 15^2 + 20^2 + 25^2

**Example #2:**

```python
da = DynamicArray([100])
print(da.reduce(lambda x, y: x + y ** 2))
print(da.reduce(lambda x, y: x + y ** 2, -1))
da.remove_at_index(0)
print(da.reduce(lambda x, y: x + y ** 2))
print(da.reduce(lambda x, y: x + y ** 2, -1))
```

**Output:**

> 100
> 9999
> None
> -1

## **find_mode**(arr: DynamicArray) -> (DynamicArray, int):

Write a standalone function outside of the DynamicArray class that receives a dynamic array already in sorted order, either non-descending or non-ascending. The function will return a tuple containing (in this order) a dynamic array comprising the mode (most-occurring) value/s of the array, and an integer that represents the highest frequency (how many times they appear).

If there is more than one value that has the highest frequency, all values at that frequency should be included in the array being returned in the order in which they appear in the input array. If there is only one mode, only that value should be included.

You may assume that the input array will contain one or more homogeneous elements(either all numbers, or strings, or custom objects, but never a mix of these). You do not need to write checks for these conditions.

For full credit, the function must be implemented with **O(N)** complexity **with no additional data structures (beyond the array you return) being created. (Note: You can replace the return array as needed)**

**Example #1:**

```python
test_cases = (
[1, 1, 2, 3, 3, 4],
[1, 2, 3, 4, 5],
["Apple", "Banana", "Banana", "Carrot", "Carrot", "Date", "Date", "Date",
"Eggplant", "Eggplant", "Eggplant", "Fig", "Fig", "Grape"]
)
for case in test_cases:
    da = DynamicArray(case)
    mode, frequency = find_mode(da)
    print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
da = DynamicArray()
for x in range(len(case)):
    da.append(case[x])
    mode, frequency = find_mode(da)
    print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

```

**Output:**

> DYN_ARR Size/Cap: 6/8 [1, 1, 2, 3, 3, 4]
> Mode: DYN_ARR Size/Cap: 2/4 [1, 3], Frequency: 2
> DYN_ARR Size/Cap: 5/8 [1, 2, 3, 4, 5]
> Mode: DYN_ARR Size/Cap: 5/8 [1, 2, 3, 4, 5], Frequency: 1
> DYN_ARR Size/Cap: 14/16 [Apple, Banana, Banana, Carrot, Carrot, Date, Date, Date, Eggplant, Eggplant, Eggplant, Fig, Fig, Grape]
> Mode: DYN_ARR Size/Cap: 2/4 [Date, Eggplant], Frequency: 3
> DYN_ARR Size/Cap: 1/4 [4]
> Mode: DYN_ARR Size/Cap: 1/4 [4], Frequency: 1
> DYN_ARR Size/Cap: 2/4 [4, 3]
> Mode: DYN_ARR Size/Cap: 2/4 [4, 3], Frequency: 1
> DYN_ARR Size/Cap: 3/4 [4, 3, 3]
> Mode: DYN_ARR Size/Cap: 1/4 [3], Frequency: 2
> DYN_ARR Size/Cap: 4/4 [4, 3, 3, 2]
> Mode: DYN_ARR Size/Cap: 1/4 [3], Frequency: 2
> DYN_ARR Size/Cap: 5/8 [4, 3, 3, 2, 2]
> Mode: DYN_ARR Size/Cap: 2/4 [3, 2], Frequency: 2
> DYN_ARR Size/Cap: 6/8 [4, 3, 3, 2, 2, 2]
> Mode: DYN_ARR Size/Cap: 1/4 [2], Frequency: 3
> DYN_ARR Size/Cap: 7/8 [4, 3, 3, 2, 2, 2, 1]
> Mode: DYN_ARR Size/Cap: 1/4 [2], Frequency: 3
> DYN_ARR Size/Cap: 8/8 [4, 3, 3, 2, 2, 2, 1, 1]
> Mode: DYN_ARR Size/Cap: 1/4 [2], Frequency: 3
> DYN_ARR Size/Cap: 9/16 [4, 3, 3, 2, 2, 2, 1, 1, 1]
> Mode: DYN_ARR Size/Cap: 2/4 [2, 1], Frequency: 3
> DYN_ARR Size/Cap: 10/16 [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
> Mode: DYN_ARR Size/Cap: 1/4 [1], Frequency: 4
