class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        left = 0
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]

            if right - left + 1 == k:
                res = max(res, currSum)
            
                currSum -= nums[left]
                left += 1
        
        return res / k