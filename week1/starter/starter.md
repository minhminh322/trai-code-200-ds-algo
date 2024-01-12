# Starter Code

- Implement a DynamicArray class by completing the skeleton code provided in the file **dynamic_array.py**. The DynamicArray class will use a StaticArray object as its underlying data storage container, and will provide many methods similar to the functionality of Python lists. Once completed, your implementation will include the following methods:

> resize()
> append()
> insert_at_index()
> remove_at_index()
> slice()
> merge()
> map()
> filter()
> reduce()

- The dynamic_array.py file also contains:
  a. the definition of DynamicArrayException, which is a custom exception that must be used in the ways described in the methods that mention it.
  b. several pre-written class methods, like is_empty(), length(), get_at_index(), and set_at_index().
  c. the find_mode() function, but this is a separate function outside the class that you will need to implement.

- The number of objects stored in the array at any given time will be between 0 and 1,000,000 inclusive. An array must allow for the storage of duplicate objects.

- Variables in the DynamicArray class are marked as private, so they may only be accessed and/or changed directly inside the class. Use the provided getter or setter methods when you need this functionality outside of the DynamicArray class.

### **RESTRICTIONS:**

You are NOT allowed to use ANY built-in Python data structures and/or their methods in any of your solutions. This includes built-in Python lists, dictionaries, or anything else. You must solve this portion of the assignment by importing and using objects of the StaticArray class (prewritten for you), and using class methods to write your solution.

You are NOT allowed to directly access any variables of the StaticArray class (e.g. _self.\_size_ or _self.\_data_). Access to StaticArray variables must be done by using the StaticArray class methods.

Don’t forget to include your **StaticArray** class from Week 0 in your project (make sure that static_array import StaticArray references the correct file when you are developing your solution).
