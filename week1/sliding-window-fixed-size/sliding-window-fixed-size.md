# Sliding Window (Fixed Size)

A fixed sliding window is to maintain two pointers that are k apart from each other and fit a certain constraint.

## Problem Statement:

> Given an array of numbers, find the maximum sum of a subarray with a fixed size k.

## Brute Force Approach:

The brute force way is to calculate the sum of all possible subarrays of size k and return the maximum sum. This approach has a time complexity of O(n^2).

```python
def maxSubarraySumBruteForce(nums, k):
    maxSum = float('-inf')
    for i in range(len(nums) - k + 1):
        currSum = sum(nums[i:i+k])
        maxSum = max(maxSum, currSum)
    return maxSum
```

## Improved Approach using Sliding Window:

We can optimize this using the sliding window technique. The idea is to maintain a window of size k and efficiently update the sum as we move through the array.

```python
# Initialize variables
def maxSubarraySum(nums, k):
    maxSum = float('-inf')
    currSum = 0
    left = 0

    for right in range(len(nums)):
        # Expand window
        currSum += nums[right]

        # Meet threshold (window size is k)
        if right - left + 1 == k:
            # Process the window
            maxSum = max(maxSum, currSum)

            # Shrink the window
            currSum -= nums[left]
            left += 1

    # The maximum sum of a subarray of size k
    return maxSum
```

## Explanation:

- maxSum: Keeps track of the maximum sum encountered so far.
- currSum: Represents the sum of elements in the current window.
- left, right: Points to the leftmost and righmost element of the current window.

The function iterates through the array, expanding the window by adding elements to currSum. When the window size reaches k, it processes the window by updating maxSum. Then, it shrinks the window by subtracting the leftmost element and moving the left pointer to the next position.

Finally, the function returns the maximum sum of a subarray of size k.

## Conclusion:

Sliding window is a powerful technique, especially when dealing with subarray problems. It helps optimize time complexity, and in this case, using a set facilitates efficient element lookup.

Remember, sliding window can have fixed and dynamic variations, and it's a valuable tool for solving a variety of problems.

# General Template

Version 1:

```python
def slidingWindowFixedSize(nums: List[int], k: int) -> int:
    res, currRes = 0, 0
    left = 0
    for right in range(len(nums)):
        # Expand window
        currRes += nums[right]
        # Meet threashold
        if right - left + 1 == k:
            # Process the window
            res = min/max(res, currRes)
            # Shrink the window
            currRes -= nums[left]
            left += 1

    return res
```

Version 2: Pre-calculate the size K first

```python
def slidingWindowFixedSizeV2(nums: List[int], k: int) -> int:
    # Part 1: Solve 1st window K, and update answer
    ans = calculate result for nums[:k]
    # Part 2: Solve the rest number from K to len(nums)
    for i range(k, len):
        update/adding s[i]             # head value
        update/substract s[i-k]        # tail value
        ans = min/max(ans, newResul)   # Update answer
    return ans
```
