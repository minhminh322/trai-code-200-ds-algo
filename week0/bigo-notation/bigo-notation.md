# Big O Notation

## Introduction

As we learn about various data structures in this course, we’ll want a way to
compare these data structures to each other. Specifically, we’ll want to be able to make an informed choice between the different data structures we might use to solve each particular problem we’re working on.

Most of the time, we’ll want to be able to compare data structures in a platform-independent way. In other words, we want to be able to compare data structures in a way that doesn’t depend on hardware, operating system, programming language, etc.

The reason we want to approach the comparison of data structures in this way is because data structures themselves are platform-independent. Indeed, for many of the problems you’ll work on, you won’t be able to predict exactly what kinds of platforms your data structures will be deployed on, so you’ll want to factor platform-specific things out of your design process.

To help make platform-independent comparisons of data structures, we’ll use a tool called complexity analysis. You might have also heard complexity analysis referred to as “big O" or "big Oh".

Complexity analysis will specifically allow us to assess a data structure or algorithm’s resource usage (i.e. runtime and memory consumption) in an abstract way that’s decoupled from platform-specific factors.

In particular, using complexity analysis, we’ll be able to better understand how a data structure or algorithm’s resource usage grows as the size of the input to that data structure or algorithm grows. We refer to this input size as **_n_**.

Here, when we talk about a data structure’s input, we typically mean the size of the collection being stored in the data structure. Thus, in this situation, n is the number of elements in that collection.

## Big O Notation

Big O notation is a tool for characterizing a function in terms of its growth rate. Specifically, big O notation is used to indicate an upper bound on that function’s growth rate. This upper bound is known as the growth order of the function (hence the “O” in “big O”) and is itself typically specified as a mathematical function.

Using big O notation, we can broadly categorize data structures and algorithms by their complexity classes. This categorization supplies one kind of excellent information: given the time it takes a method (implementing an algorithm) to solve a problem of size **_n_**, we can easily compute how long it would take to solve a problem of size **_2n_**.

As we work on assessing data structures and algorithms via complexity analysis, we’ll find that there are particular growth order functions we’ll encounter over and over. Some of these growth order functions and their common names are, from fastest to slowest:

O(1) – constant complexity
O(log n) – logarithmic complexity
O(sqrt(n)) – fractional power complexity
O(n) – linear complexity
O(nlogn) - linearithmic, loglinear, quasilinear, or "nlogn" complexity
O(n^2) – quadratic complexity
O(n^3) – cubic complexity
O(2n) – exponential complexity
O(n!) – factorial complexity

![Big Oh Notation](https://cdn-media-1.freecodecamp.org/images/1*KfZYFUT2OKfjekJlCeYvuQ.jpeg)

This illustration shows the differences in these complexities visually. You can see that **_nlogn_** starts getting pretty steep, but that is somewhat misleading. It's actually a pretty usable time complexity usually. But anything more than that and things start getting really bad.
