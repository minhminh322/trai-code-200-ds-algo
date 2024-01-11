from static_array import *

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    left = 0
    right = arr.length() - 1

    while left < right:
        left_var = arr[left] 
        arr[left] = arr[right]
        arr[right] = left_var
        left += 1
        right -= 1

# ------------------- TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)