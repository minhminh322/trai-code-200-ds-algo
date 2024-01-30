# Stacks

## Introduction

A stack is a data structure that follows the Last In, First Out (LIFO) principle. Think of it like a stack of plates at a buffet — you can only add or remove plates from the top. In programming, stacks are dynamic structures that support operations such as push, pop, and peek.

## Stack Operation

### Push

- **push** adds an element to the top of the stack.
- In a dynamic array, it's like appending an element to the end.
- It's an efficient O(1) operation.

### Pop

- **pop** removes the last element from the top of the stack.
- Similar to retrieving the last element in a dynamic array.
- Also an efficient O(1) operation.

### Peek

- **peek** returns the top element of the stack without removing it.
- Retrieving the last element in the stack

## Summary

- Push: O(1)
- Pop: O(1)\* (Check if empty first)
- Peek: O(1)\* (Retrieves without removing)

Stacks are versatile and can be used for various applications, such as reversing sequences like strings. The key takeaway is the LIFO behavior — the last element you add is the first one to be removed.
