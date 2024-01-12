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

Example #2:

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
