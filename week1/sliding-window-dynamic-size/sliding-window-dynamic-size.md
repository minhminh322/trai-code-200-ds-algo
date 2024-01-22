# Sliding Window (Dynamic Size)

Sliding Window (Dynamic Size) tells us that we can keep expanding our window as long as we don't break the constraint we are given

## Problem Statement:

> Find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive.

## Brute Force Approach:

In this brute force solution, we iterate through each starting index i and calculate the sum of subarrays starting from i. We check if the sum is greater than or equal to the target and update the minimum length accordingly. The nested loop helps us explore all possible subarrays.
However, it's important to note that the time complexity of this brute force approach is O(n^2), where n is the length of the input array.

```python
def shortestSubarrayBruteForce(nums, target):
    min_length = float('inf')

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]

            if current_sum >= target:
                min_length = min(min_length, j - i + 1)
                break  # No need to continue checking longer subarrays

    return 0 if min_length == float('inf') else min_length

```

## Improved Approach using Sliding Window:

We can optimize this using the sliding window technique. We will expand our window from the right and if our sum becomes greater than or equal to the target, we will start removing from the left until it no longer breaks this constraint.
This solution has a time complexity of O(n) as it performs a single pass through the array, making it more efficient compared to the brute force approach.

```python
# Initialize variables
def shortestSubarray(nums, target):
    L, total = 0, 0
    min_length = float('inf')

    for R in range(len(nums)):
        total += nums[R]

        while total >= target:
            min_length = min(min_length, R - L + 1)
            total -= nums[L]
            L += 1

    return 0 if min_length == float('inf') else min_length

```

## Explanation:

We use two pointers (L and R) to maintain a window. We start with an empty window and gradually expand it from the right (R). If the sum within the window becomes greater than or equal to the target, we update the minimum length and then shrink the window from the left (L) until the constraint is met.

## Conclusion:

Sliding window is a powerful technique, especially when dealing with subarray problems. It helps optimize time complexity, and in this case, using a set facilitates efficient element lookup.

Remember, sliding window can have fixed and dynamic variations, and it's a valuable tool for solving a variety of problems.

# General Template

Version 1:

```python
def slidingWindowDynamicSize(nums: List[int], target: int) -> int:
    # Initialize pointers and other necessary variables
    res, currRes = 0, 0
    left = 0

    for right in range(len(nums)):
        # Expand window
        currRes += nums[right]

        # Adjust the window and update result if the constraint is met
        while res >= target:
            res = min,ax(res, right - left + 1)
            currRes -= nums[left]
            left += 1

    return res

```
