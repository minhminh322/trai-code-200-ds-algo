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
