import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr):
    if arr.length() == 0:
        return None  # Handle empty array case

    min_val = max_val = arr[0]
    for index in range(1, arr.length()):  # Start the loop from index 1
        if arr[index] < min_val:
            min_val = arr[index]
        elif arr[index] > max_val:
            max_val = arr[index]
    return [min_val, max_val]

def fizz_buzz(arr):
    fizz_arr = StaticArray(arr.length())
    for index in range(arr.length()):
        num = arr[index]
        if num % 3 == 0 and num % 5 == 0:
            fizz_arr[index] = 'fizzbuzz'
        elif num % 3 == 0:
            fizz_arr[index] = 'fizz'
        elif num % 5 == 0:
            fizz_arr[index] = 'buzz'
        else:
            fizz_arr[index] = num
    return fizz_arr

def reverse(arr):
    left = 0
    right = arr.length() - 1

    while left < right:
        left_var = arr[left] 
        arr[left] = arr[right]
        arr[right] = left_var
        left += 1
        right -= 1

def rotate(arr, steps):
    if arr.length() <= 1:
        return arr  # No need to rotate

    steps = steps % arr.length()  # Handle large steps by taking modulo
    rotate_arr = StaticArray(arr.length())
    for index in range(arr.length()):
        new_index = (index + steps) % arr.length()
        rotate_arr[index] = arr[new_index]
    return rotate_arr

def sa_range(start, end):
    if start < end:
        length = end - start + 1
    else:
        length = start - end + 1
    range_arr = StaticArray(length)
    for index in range(0, length):
        if start < end:
            range_arr[index] = start + index
        else:
            range_arr[index] = start - index
    return range_arr



def is_sorted(arr):
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


def find_mode(arr):
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


def remove_duplicates(arr):
    if arr.length() <= 1:
        return arr  # No duplicates to remove
    
    new_arr = StaticArray(arr.length())
    new_arr_index = 0
    new_arr[0] = arr[0]
    for i in range(1, arr.length()):
        if new_arr[new_arr_index] != arr[i]:
            new_arr_index += 1
            new_arr[new_arr_index] = arr[i]
    
    return new_arr

def count_sort(arr):
    if arr.length() == 0:
        return arr  # Handle empty array case

    min_val = max_val = arr[0]
    for index in range(arr.length()):
        if min_val > arr[index]:
            min_val = arr[index]
        if max_val < arr[index]:
            max_val = arr[index]

    arr_range = max_val - min_val + 1
    count_arr = StaticArray(arr_range)  
    for i in range(count_arr.length()):
        count_arr[i] = 0 # Initialize count_arr with zeros

    for index in range(arr.length()):
        count_arr[arr[index] - min_val] += 1

    result_arr = StaticArray(arr.length())
    result_index = 0
    for i in range(count_arr.length() - 1, -1, -1):
        count = count_arr[i]
        while count > 0:
            result_arr[result_index] = i + min_val
            result_index += 1
            count -= 1

    return result_arr

def sorted_squares(arr):
    squares_arr = StaticArray(arr.length())
    left, right = 0, arr.length() - 1
    squares_arr_index = squares_arr.length() - 1
    while left <= right:
        if arr[left] ** 2 < arr[right] ** 2:
            squares_arr[squares_arr_index] = arr[right] ** 2
            right -= 1
        else:
            squares_arr[squares_arr_index] = arr[left] ** 2
            left += 1
        squares_arr_index -= 1
        
    return squares_arr

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

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

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

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

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
