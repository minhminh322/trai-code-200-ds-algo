# Queues

## Introduction

Queues are data structures that follow the First In, First Out (FIFO) principle. Imagine a line at a bank — the first person to join the line is the first to be served. In software, queues are essential for scenarios like print jobs, where tasks are handled on a first-come, first-served basis.

## Queue Operation

The most common implementation of a queue is using a Linked List. Two primary operations supported by queues are enqueue and dequeue.

### Enqueue

- **enqueue** adds elements to the tail of the queue.
- It's an O(1) operation since adding to the end of the queue requires no shifting of elements.

### Dequeue

- **dequeue** removes elements from the front of the queue and returns that element.
- It's an O(1) operation.

## Queue Implementation with Dynamic Arrays

Queues can also be implemented using dynamic arrays. However, maintaining the efficiency of both enqueue and dequeue operations becomes trickier. With the array implementation, dequeue could take O(n) time due to shifting of elements.

As with stacks, it's crucial to check if the queue is empty before performing a dequeue operation.

## Double-Ended Queue (Deque)

There's a variation of the queue called deque (pronounced "deck"), which allows adding and removing elements from both the head and the tail.

## Summary

- Enqueue: O(1)
- Dequeue: O(1)

Queues are crucial for tasks like breadth-first search for trees and graphs, a concept we'll explore later in the course. They play a fundamental role in managing and processing data in a sequential manner.
