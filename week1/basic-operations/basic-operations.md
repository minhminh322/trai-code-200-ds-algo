# Basic Operations

## **resize**(self, new_capacity: int) -> None:

This method changes the underlying storage capacity for the elements in the dynamic array. It does not change the values or the order of any elements currently stored in the array.

It is intended to be an “internal” method of the DynamicArray class, called by other class methods such as **append(), remove_at_index(), or insert_at_index()**, to manage the capacity of the underlying data structure.

The method should only accept positive integers for **new_capacity**. Additionally, new_capacity cannot be smaller than the number of elements currently stored in the dynamic array (which is tracked by the self.\_size variable). If new_capacity is not a positive integer, or if new_capacity is less than self.\_size, this method should not do any work and immediately exit.

**Example #1:**

```python
da = DynamicArray()
da.print_da_variables()
da.resize(8)
da.print_da_variables()
da.resize(2)
da.print_da_variables()
da.resize(0)
da.print_da_variables()
```

**Output:**

> Length: 0, Capacity: 4, STAT_ARR Size: 4 [None, None, None, None]
> Length: 0, Capacity: 8, STAT_ARR Size: 8 [None, None, None, None, None, None, None, None]
> Length: 0, Capacity: 2, STAT_ARR Size: 2 [None, None]
> Length: 0, Capacity: 2, STAT_ARR Size: 2 [None, None]
> NOTE: Example 2 below will not work properly unless the append() method is implemented.

**Example #2:**

```python
da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
print(da)
da.resize(20)
print(da)
da.resize(4)
print(da)
```

**Output:**

> DYN_ARR Size/Cap: 8/8 [1, 2, 3, 4, 5, 6, 7, 8]
> DYN_ARR Size/Cap: 8/20 [1, 2, 3, 4, 5, 6, 7, 8]
> DYN_ARR Size/Cap: 8/20 [1, 2, 3, 4, 5, 6, 7, 8]

## **append**(self, value: object) -> None:

This method adds a new value at the end of the dynamic array. If the internal storage associated with the dynamic array is already full, you will need to DOUBLE its capacity before adding a new value (hint: you should use your already written resize() function for this).

**Example #1:**

```python
da = DynamicArray()
da.print_da_variables()
da.append(1)
da.print_da_variables()
print(da)
```

**Output:**

> Length: 0, Capacity: 4, STAT_ARR Size: 4 [None, None, None, None]
> Length: 1, Capacity: 4, STAT_ARR Size: 4 [1, None, None, None]
> DYN_ARR Size/Cap: 1/4 [1]

**Example #2:**

```python
da = DynamicArray()
for i in range(9):
    da.append(i + 101)
print(da)
```

**Output:**

> DYN_ARR Size/Cap: 1/4 [101]
> DYN_ARR Size/Cap: 2/4 [101, 102]
> DYN_ARR Size/Cap: 3/4 [101, 102, 103]
> DYN_ARR Size/Cap: 4/4 [101, 102, 103, 104]
> DYN_ARR Size/Cap: 5/8 [101, 102, 103, 104, 105]
> DYN_ARR Size/Cap: 6/8 [101, 102, 103, 104, 105, 106]
> DYN_ARR Size/Cap: 7/8 [101, 102, 103, 104, 105, 106, 107]
> DYN_ARR Size/Cap: 8/8 [101, 102, 103, 104, 105, 106, 107, 108]
> DYN_ARR Size/Cap: 9/16 [101, 102, 103, 104, 105, 106, 107, 108, 109]

**Example #3:**

```python
da = DynamicArray()
for i in range(600):
    da.append(i)
print(da.length())
print(da.get_capacity())
```

**Output:**

> 600
> 1024

## **insert_at_index**(self, index: int, value: object) -> None:

This method adds a new value at the specified index in the dynamic array. Index 0 refers to the beginning of the array. If the provided index is invalid, **this method must raise a custom “DynamicArrayException”.** If the array contains N elements, valid indices for this method are [0, N] inclusive.
If the internal storage associated with the dynamic array is already full, you will need to DOUBLE its capacity before adding a new value.

**Example #1:**

```python
da = DynamicArray([100])
print(da)
da.insert_at_index(0, 200)
da.insert_at_index(0, 300)
da.insert_at_index(0, 400)
print(da)
da.insert_at_index(3, 500)
print(da)
da.insert_at_index(1, 600)
print(da)
```

**Output:**

> DYN_ARR Size/Cap: 1/4 [100]
> DYN_ARR Size/Cap: 4/4 [400, 300, 200, 100]
> DYN_ARR Size/Cap: 5/8 [400, 300, 200, 500, 100]
> DYN_ARR Size/Cap: 6/8 [400, 600, 300, 200, 500, 100]

**Example #2:**

```python
da = DynamicArray() try:
    da.insert_at_index(-1, 100)
except Exception as e:
    print("Exception raised:", type(e))
da.insert_at_index(0, 200)
try:
    da.insert_at_index(2, 300)
except Exception as e:
    print("Exception raised:", type(e))
print(da)
```

**Output:**

> Exception raised: <class '**main**.DynamicArrayException'>
> Exception raised: <class '**main**.DynamicArrayException'>
> DYN_ARR Size/Cap: 1/4 [200]

**Example #3:**

```python
da = DynamicArray()
for i in range(1, 10):
    index, value = i - 4, i * 10
    try:
        da.insert_at_index(index, value)
    except Exception as e:
        print("Cannot insert value", value, "at index", index)
print(da)
```

**Output:**

> Cannot insert value 10 at index -3
> Cannot insert value 20 at index -2
> Cannot insert value 30 at index -1
> DYN_ARR Size/Cap: 6/8 [40, 50, 60, 70, 80, 90]

## **remove_at_index**(self, index: int) -> None:

This method removes the element at the specified index in the dynamic array. Index 0 refers to the beginning of the array. If the provided index is invalid, **this method must raise a custom “DynamicArrayException”.** If the array contains N elements, valid indices for this method are [0, N - 1] inclusive.

When the number of elements stored in the array (before removal) is STRICTLY LESS THAN 1⁄4 of its current capacity, the capacity must be reduced to TWICE the number of current elements. This check and capacity adjustment must occur BEFORE removal of the element.

If the current capacity (before reduction) is 10 elements or less, reduction should not occur at all. If the current capacity (before reduction) is greater than 10 elements, the reduced capacity cannot become less than 10 elements. Please see the examples below, especially example #3, for clarification.

Future methods will depend on this being able to run in **O(1) best case.**

**Example #1:**

```python
da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
print(da)
da.remove_at_index(0)
print(da)
da.remove_at_index(6)
print(da)
da.remove_at_index(2)
print(da)
```

**Output:**

> DYN_ARR Size/Cap: 8/8 [10, 20, 30, 40, 50, 60, 70, 80]
> DYN_ARR Size/Cap: 7/8 [20, 30, 40, 50, 60, 70, 80]
> DYN_ARR Size/Cap: 6/8 [20, 30, 40, 50, 60, 70]
> DYN_ARR Size/Cap: 5/8 [20, 30, 50, 60, 70]

**Example #2:**

```python
da = DynamicArray([1024])
print(da)
for i in range(17):
    da.insert_at_index(i, i)
print(da.length(), da.get_capacity())
for i in range(16, -1, -1):
    da.remove_at_index(0)
print(da)

```

**Output:**

> DYN_ARR Size/Cap: 1/4 [1024]
> 18 32
> DYN_ARR Size/Cap: 1/10 [1024]

**Example #3:**

```python
da = DynamicArray()
print(da.length(), da.get_capacity())
[da.append(1) for i in range(100)]
print(da.length(), da.get_capacity())	# step 1 - add 100 elements
[da.remove_at_index(0) for i in range(68)]
print(da.length(), da.get_capacity())	# step 2 - remove 68 elements
da.remove_at_index(0)
print(da.length(), da.get_capacity())	# step 3 - remove 1 element
da.remove_at_index(0)
print(da.length(), da.get_capacity())	# step 4 - remove 1 element
[da.remove_at_index(0) for i in range(14)]
print(da.length(), da.get_capacity())	# step 5 - remove 14 elements
da.remove_at_index(0)
print(da.length(), da.get_capacity())	# step 6 - remove 1 element
da.remove_at_index(0)
print(da.length(), da.get_capacity())	# step 7 - remove 1 element

for i in range(14):
    print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
    da.remove_at_index(0)
    print(" After remove_at_index(): ", da.length(), da.get_capacity())

```

**Output:**

> 0 4
> 100 128
> 32 128
> 31 128
> 30 62
> 16 62
> 15 62
> 14 30
> Before remove_at_index(): 14 30 After remove_at_index(): 13 30
> Before remove_at_index(): 13 30 After remove_at_index(): 12 30
> Before remove_at_index(): 12 30 After remove_at_index(): 11 30
> Before remove_at_index(): 11 30 After remove_at_index(): 10 30
> Before remove_at_index(): 10 30 After remove_at_index(): 9 30
> Before remove_at_index(): 9 30 After remove_at_index(): 8 30
> Before remove_at_index(): 8 30 After remove_at_index(): 7 30
> Before remove_at_index(): 7 30 After remove_at_index(): 6 14
> Before remove_at_index(): 6 14 After remove_at_index(): 5 14
> Before remove_at_index(): 5 14 After remove_at_index(): 4 14
> Before remove_at_index(): 4 14 After remove_at_index(): 3 14
> Before remove_at_index(): 3 14 After remove_at_index(): 2 10
> Before remove_at_index(): 2 10 After remove_at_index(): 1 10
> Before remove_at_index(): 1 10 After remove_at_index(): 0 10

**Example #4:**

```python
da = DynamicArray([1, 2, 3, 4, 5])
print(da)
for _ in range(5):
    da.remove_at_index(0)
    print(da)

```

**Output:**

> DYN_ARR Size/Cap: 5/8 [1, 2, 3, 4, 5]
> DYN_ARR Size/Cap: 4/8 [2, 3, 4, 5]
> DYN_ARR Size/Cap: 3/8 [3, 4, 5]
> DYN_ARR Size/Cap: 2/8 [4, 5]
> DYN_ARR Size/Cap: 1/8 [5]
> DYN_ARR Size/Cap: 0/8 []
