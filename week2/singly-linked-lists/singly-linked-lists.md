# Introduction to LinkedList

## Introduction

In this exploration, we will introduce linked lists, which you may or may not have seen before. Most often, when you make lists or other types of collections, the default tends to be an array (a contiguous block of memory). Linked lists don’t use this paradigm. Instead, linked lists typically allocate a distinct block of memory for each element and then have one element keep track of the next, thereby forming a chain of links.

## Why Linked Lists?

Why might we want to use linked lists? They come with some interesting advantages. Think back to the discussion of dynamic arrays. Every so often, we need to resize the array. Oftentimes, this is fine. But in some applications, a long pause to resize an array is unacceptable. Think about the controller for an autonomous car or aircraft. A long pause at the wrong moment could be disastrous.

Linked lists never suffer from this issue. We can always add and remove from the start of the linked list in constant time, which is pretty much the best any operation can hope for. Some kinds of linked lists allow us to add or remove from the front or the back of the list.

There are, however, some drawbacks. It takes a long time to access elements in the middle of the list. We can’t just perform a simple multiplication to find an element's location. Instead, we have to follow each link until we arrive at the element we want. Also, we need to use a bit of space for each link. If we are storing very small pieces of data, like integers, this can potentially double the amount of memory used.

This means that linked lists tend to be good for implementing ADTs where we only do operations at the ends of a structure. They also require a little extra memory to hold our data.

## Singly Linked Lists

Linked lists (like dynamic arrays) are a linear data structure. In other words, data in a linked list (like data in a dynamic array) forms a linear sequence, with the individual data elements placed one after the other within the data structure. Like an array, a linked list arranges the items in a particular order, which means each item has a certain position in the list.

A linked list differs from a dynamic array, however, in that each individual value is stored in its own small structure called a node. These individual nodes are chained together into a sequence own small structure called a node. These individual nodes are chained together into a sequence with each one “pointing” to the next (and sometimes also the previous) node in the list.

In other words, each node in a linked list stores exactly one value and (at minimum) points to the next link in the list. Thus, a simple node structure needs at least two fields:

- value: This is where the value associated with the node is stored.
- next: This points to the next node in the list (or to None , if there is no next node).

A linked list in which each node points only to the next node is known as a singly linked list. A linked list will contain a node for each value stored in the list, although there may be other nodes that serve purely structural purposes. Nodes are allocated and freed as values are added and removed from the list.

The simplest form of a linked list only keeps track of the first element in the list, which is known as the head. For example, here’s what a singly linked list would look like if we were keeping track of just the head (e.g., in a variable named head):

![image](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200922124319/Singly-Linked-List1.png)

There are several possible ways we can implement a simple singly linked list. One of these involves keeping track of both the head and the tail of the list (or last element). This allows us to have easy access to both ends of the list. It would look something like this:

![image](https://www.cs.usfca.edu/~srollins/courses/cs112-f07/web/notes/linkedlists/ll3.gif)
