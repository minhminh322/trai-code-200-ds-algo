from static_array import *

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    ascending_result = descending_result = True
    for index in range(1, arr.length()):
        if arr[index] < arr[index - 1]:
            ascending_result = False
        elif arr[index] > arr[index - 1]:
            descending_result = False
        else:
            ascending_result = descending_result = False
    
    if ascending_result:
        return 1
    elif descending_result:
        return -1
    else:
        return 0

# ------------------- TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")