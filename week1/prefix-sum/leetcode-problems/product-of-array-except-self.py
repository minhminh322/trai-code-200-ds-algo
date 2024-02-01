class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = [], [0]*len(nums)
        currSum = 1
        for i in range(len(nums)):
            currSum *= nums[i]
            leftSum.append(currSum)
        # Reset value
        currSum = 1
        for i in range(len(nums) - 1, -1, -1):
            currSum *= nums[i]
            rightSum[i] = currSum
        
        res = []
        for i in range(len(nums)):
            left = leftSum[i-1] if i > 0 else 1
            right = rightSum[i+1] if i < len(nums)-1 else 1
            res.append(left * right)

        return res