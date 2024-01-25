# Singly Linked Lists Implementation

## insert_front(self, value: object) -> None:

This method adds a new node at the beginning of the list (right after the front sentinel). It must be implemented with O(1) runtime complexity.

**Example #1:**

```python
test_case = ["A", "B", "C"]
lst = LinkedList()
for case in test_case:
    lst.insert_front(case)
    print(lst)
```

**Output:**

> SLL [A]
> SLL [B -> A]
> SLL [C -> B -> A]

## insert_back(self, value: object) -> None:

This method adds a new node at the end of the list. It must be implemented with O(N) runtime complexity.

**Example #1:**

```python
test_case = ["C", "B", "A"]
lst = LinkedList()
for case in test_case:
    lst.insert_back(case)
    print(lst)
```

**Output:**

> SLL [C]
> SLL [C -> B]
> SLL [C -> B -> A]

## insert_at_index(self, index: int, value: object) -> None:

This method inserts a new value at the specified index position in the linked list. Index 0 refers to the beginning of the list (right after the front sentinel).
If the provided index is invalid, the method must raise a custom “SLLException”. If the linked list contains N nodes (the sentinel node is not included in this count), valid indices for this method are [0, N] inclusive. It must be implemented with O(N) runtime complexity.

**Example #1:**

```python
lst = LinkedList()
test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
for index, value in test_cases:
    print("Inserted", value, "at index", index, ": ", end="")
    try:
        lst.insert_at_index(index, value)
        print(lst)
    except Exception as e:
        print(type(e))

```

**Output:**

> Inserted A at index 0 : SLL [A]
> Inserted B at index 0 : SLL [B -> A]
> Inserted C at index 1 : SLL [B -> C -> A]
> Inserted D at index 3 : SLL [B -> C -> A -> D]
> Inserted E at index -1 : <class '**main**.SLLException'>
> Inserted F at index 5 : <class '**main**.SLLException'>

## remove_at_index(self, index: int) -> None:

This method removes the node at the specified index position from the linked list. Index 0 refers to the beginning of the list (right after the front sentinel).
If the provided index is invalid, the method must raise a custom “SLLException”. If the list contains N elements (the sentinel node is not included in this count), valid indices for this method are [0, N - 1] inclusive. It must be implemented with O(N) runtime complexity.

**Example #1:**

```python
lst = LinkedList([1, 2, 3, 4, 5, 6])
print(f"Initial LinkedList : {lst}")
for index in [0, 2, 0, 2, 2, -2]:
    print("Removed at index:", index, ": ", end="")
    try:
        lst.remove_at_index(index)
        print(lst)
    except Exception as e:
        print(type(e))
print(lst)

```

**Output:**

> Initial LinkedList : SLL [1 -> 2 -> 3 -> 4 -> 5 -> 6]
> Removed at index 0 : SLL [2 -> 3 -> 4 -> 5 -> 6]
> Removed at index 2 : SLL [2 -> 3 -> 5 -> 6]
> Removed at index 0 : SLL [3 -> 5 -> 6]
> Removed at index 2 : SLL [3 -> 5]
> Removed at index 2 : <class '**main**.SLLException'>
> Removed at index -2 : <class '**main**.SLLException'>

## remove(self, value: object) -> bool:

This method traverses the list from the beginning to the end, and removes the first node that matches the provided value. The method returns True if a node was removed from the list. Otherwise, it returns False. It must be implemented with O(N) runtime complexity.

**Example #1:**

```python
lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
print(f"Initial LinkedList, Length: {lst.length()}\n	{lst}")
for value in [7, 3, 3, 3, 3]:
    print(f"remove({value}): {lst.remove(value}, Length: {lst.length()}" f"\n {lst}")

```

**Output:**

> Initial LinkedList, Length: 9
> SLL [1 -> 2 -> 3 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3]
> remove(7): False, Length: 9
> SLL [1 -> 2 -> 3 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3]
> remove(3): True, Length: 8
> SLL [1 -> 2 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3]
> remove(3): True, Length: 7
> SLL [1 -> 2 -> 1 -> 2 -> 1 -> 2 -> 3]
> remove(3): True, Length: 6
> SLL [1 -> 2 -> 1 -> 2 -> 1 -> 2]
> remove(3): False, Length: 6
> SLL [1 -> 2 -> 1 -> 2 -> 1 -> 2]

**Example #2:**

```python
lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
print(f"Initial LinkedList, Length: {lst.length()}\n {lst}")
for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
    print(f"remove({value}): {lst.remove(value), Length: {lst.length()}" f"\n {lst}")

```

**Output:**

> Initial LinkedList, Length: 9
> SLL [1 -> 2 -> 3 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3]
> remove(1): True, Length: 8
> SLL [2 -> 3 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3]
> remove(2): True, Length: 7
> SLL [3 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3]
> remove(3): True, Length: 6
> SLL [1 -> 2 -> 3 -> 1 -> 2 -> 3]
> remove(1): True, Length: 5
> SLL [2 -> 3 -> 1 -> 2 -> 3]
> remove(2): True, Length: 4
> SLL [3 -> 1 -> 2 -> 3]
> remove(3): True, Length: 3
> SLL [1 -> 2 -> 3]
> remove(3): True, Length: 2
> SLL [1 -> 2]
> remove(2): True, Length: 1
> SLL [1]
> remove(1): True, Length: 0
> SLL []

## count(self, value: object) -> int:

This method counts the number of elements in the list that match the provided value. The
method then returns this number. It must be implemented with O(N) runtime complexity.

**Example #1:**

```python
lst = LinkedList([1, 2, 3, 1, 2, 2])
print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
```

**Output:**

> SLL [1 -> 2 -> 3 -> 1 -> 2 -> 2] 2 3 1 0

## find(self, value: object) -> bool:

This method returns a Boolean value based on whether or not the provided value exists in
the list. It must be implemented with O(N) runtime complexity.

**Example #1:**

```python
lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
print(lst)
print(lst.find("Waldo"))
print(lst.find("Superman"))
print(lst.find("Santa Claus"))
```

**Output:**

> SLL [Waldo -> Clark Kent -> Homer -> Santa Claus]
> True
> False
> True

## slice(self, start_index: int, size: int) -> "LinkedList":

This method returns a new LinkedList that contains the requested number of nodes from the original list, starting with the node located at the requested start index. If the original list contains N nodes, a valid start_index is in range [0, N - 1] inclusive. The original list cannot be modified. The runtime complexity of your implementation must be O(N).
You are allowed to directly access the variable (\_head) of LinkedList objects you create. If the provided start index is invalid, or if there are not enough nodes between the start index and the end of the list to make a slice of the requested size, this method raises a custom “SLLException”.

**Example #1:**

```python
lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
ll_slice = lst.slice(1, 3)
print("Source:", lst)
print("Start: 1 Size: 3 :", ll_slice)
ll_slice.remove_at_index(0)
print("Removed at index 0 :", ll_slice)
```

**Output:**

> Source: SLL [1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9]
> Start: 1 Size: 3 : SLL [2 -> 3 -> 4]
> Removed at index 0 : SLL [3 -> 4]

**Example #2:**

```python
lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
print("Source:", lst)
slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
for index, size in slices:
    print("Start:", index, "Size:", size, end="")
    try:
        print(" :", lst.slice(index, size))
    except:
        print(" : exception occurred.")
```

**Output:**

> Source: SLL [10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16]
> Start: 0 Size: 7 : SLL [10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16]
> Start: -1 Size: 7 : exception occurred.
> Start: 0 Size: 8 : exception occurred.
> Start: 2 Size: 3 : SLL [12 -> 13 -> 14]
> Start: 5 Size: 0 : SLL []
> Start: 5 Size: 3 : exception occurred.
> Start: 6 Size: 1 : SLL [16]
