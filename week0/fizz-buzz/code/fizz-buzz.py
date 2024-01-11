from static_array import *

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
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

# ------------------- TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)