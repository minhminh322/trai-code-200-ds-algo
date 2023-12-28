**Summary**

For this assignment, you will write a few short Python functions. The primary objectives are to ensure that:

- You are familiar with basic Python syntax constructs
- Your programming environment is set up correctly
- You are familiar with submitting assignments through Gradescope, and troubleshooting your solutions based on Gradescope output
- You know how to import and use classes that have been pre-written for you

For this course, we assume you are comfortable with:

- Iterating over a list of elements usingfor andwhile loops
- Accessing elements in a list or array using their indices
- Passing functions as parameters to other functions
- Using classes pre-written for you (imported into your code to create objects)
- Writing your own classes (including extending existing classes)
- Writing unit tests for your code
- Debugging your solutions

None of the functions in this assignment, will require Python knowledge beyond what was covered in CS50x Course. If you completed the CS50x classes, you should be able to complete this assignment.

**General Instructions**

1. You will be provided with a starter “skeleton” code, on which you will build your implementation. Methods defined in the skeleton code must retain their names and input/output parameters. Variables defined in the skeleton code must also retain their names. We will only test your solution by making calls to methods defined in the skeleton code, and by checking values of variables defined in the skeleton code. You are allowed to:

   - add more helper methods and variables, as needed
   - add optional default parameters to method definitions
   - modify or add to the basic testing section within the scope of:

  ```python 
  if \_\_name\_\_ == "\_\_main\_\_":
   ```

   **However, certain classes and methods cannot be changed in any way.** Please see the comments in the skeleton code for guidance. The content of any methods pre-written for you as part of the skeleton code must not be changed.!

2. The skeleton code and code examples provided in this document are part of assignment requirements. Please read all of them very carefully. They have been carefully selected to demonstrate requirements for each method. Refer to them for detailed descriptions of expected method behavior, input/output parameters, and handling of edge cases.

3. **For each method, you are required to use an iterative solution**. Recursion is not permitted.

4. Unless indicated otherwise, we will test your implementation with different types of objects, not just integers. We guarantee that all such objects will have correct implementation of:
   a. [“rich comparison” methods](https://docs.python.org/3/reference/datamodel.html#object.__lt__): 1. \_\_eq\_\_() 2. \_\_lt\_\_() 3. \_\_gt\_\_() 4. \_\_ge\_\_() 5. \_\_le\_\_()
   b. [**str**()](https://docs.python.org/3/reference/datamodel.html#object.__str__)!

**Specific Instructions**

There are 10 separate problems in this assignment. For each problem, you will write a Python function according to the provided specifications. The skeleton code and some basic test cases for each problem are provided in the exercise.

Most problems will take as input (and sometimes return as output) an object of the StaticArray class. The StaticArray class has been pre-written for you, and is located in the file static_array.py

StaticArray is a very simple class that simulates the behavior of a fixed size array. It has only four methods, and contains code to support bracketed indexing ([]):

    1) init() - Creates a new static array that will store a fixed number of elements. Once the StaticArray is created, its size cannot be changed.
    2) set() - Changes the value of any element using its index.
    3) get() - Reads the value of any element using its index.
    4) length() - Queries the number of elements in the array.

Please review the code and comments in the StaticArray class to better understand the available methods, their use, and input/output parameters. Note that since StaticArray is intentionally a very simple class, it does not possess the many capabilities typically associated with Python lists. You need to write your solutions using only the available StaticArray functionality, as described above.

**RESTRICTIONS:** You are NOT allowed to use ANY built-in Python data structures and/or their methods in any of your solutions. This includes built-in Python lists, dictionaries, or anything else. Variables for holding a single value, or a tuple holding at most three values, are allowed. It is also OK to userange().

You are NOT allowed to directly access any variables of the StaticArray class (e.g. self.\_size orself.\_data). Access to StaticArray variables must be done by using the StaticArray class methods.
