# The brute force way is to calculate the sum of all possible subarrays of size k 
# and return the maximum sum. This approach has a time complexity of O(n^2).

def maxSubarraySumBruteForce(nums, k):
    maxSum = float('-inf')
    for i in range(len(nums) - k + 1):
        currSum = sum(nums[i:i+k])
        maxSum = max(maxSum, currSum)
    return maxSum

# Improved Approach using Sliding Window
# Version 1
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

# Version 2:  Pre-calculate the size K first
def maxSubarraySumV2(nums, k):
    # Solve 1st window K, and update answer
    maxSum = sum(nums[:k])
    currSum = maxSum
    
    for i in range(k, len(nums)):
        # Update head value
        currSum += nums[i]
        # Update tail value
        currSum -= nums[i - k]
        # Update answer
        maxSum = max(maxSum, currSum)

    return maxSum
