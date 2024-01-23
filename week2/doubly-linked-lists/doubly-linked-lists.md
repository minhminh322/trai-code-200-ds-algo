# Doubly Linked Lists

Another type of linked list is what’s known as a doubly linked list. In a doubly linked list, each node keeps track of both the next node and the previous node:

![image](https://miro.medium.com/v2/resize:fit:556/1*hP1fUYWY1-KSXUgv4tl1Hg.png)

In a doubly linked list, it’s easy to iterate both forward and backward; whereas in a singly linked list, it’s only practical to move forward from one node to the next.

# Sentinel Nodes

Another implementation option for linked lists are sentinel nodes (also known as headers). These nodes help us handle special cases, such as operations at the start of a linked list, or when a linked list is empty. Basically, they are nodes that hold a piece of data that indicates it is the start or end of the linked list. Sentinel nodes differ from the head of a linked list, in that their data isn't actually used in the program. For example, they might hold None data in Python.
When a program references a linked list, it will point to the first node. When there is a sentinel node, it will point to the sentinel, and then the sentinel will point to the first node with actual data.
In the case of an empty list, the starting sentinel will point to the ending sentinel (if one is being used). The ending sentinel will often just point to None to indicate it is the last node.
A populated list with sentinels might look like this:

![image](https://2896152755-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LFrWzEqLSRHjU6HG9dw%2F-LMdyQ7AvAWR9WA6KQD4%2F-LMe-5ZsVky5maKnQyWe%2Fsentinelpush2.png?alt=media&token=f44d793c-9489-442b-8c55-a60d5890ded7)
