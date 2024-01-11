from static_array import *

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    if arr.length() == 0:
        return None, 0  # Handle empty array case

    count = 1
    mode = arr[0]
    i = 0
    while i < arr.length():
        j = i + 1  # Start j from i + 1
        while j < arr.length() and arr[j] == arr[i]:
            count += 1
            j += 1
        
        if j - i > count:
            count = j - i
            mode = arr[i]
        i = j

    return mode, count

# ------------------- TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")