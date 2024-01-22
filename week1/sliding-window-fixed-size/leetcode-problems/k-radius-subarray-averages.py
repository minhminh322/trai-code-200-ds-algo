class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        left, currSum = 0, 0

        for right in range(len(nums)):
            currSum += nums[right]

            if right - left + 1 == 2*k + 1:
                res[right - k] = currSum // (2*k + 1)
                
                currSum -= nums[left]
                left += 1
        
        return res

