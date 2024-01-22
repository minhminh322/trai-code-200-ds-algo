class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        currSum = 0
        left = 0

        for right in range(len(nums)):
            # add R to sum
            currSum += nums[right]
            # check if reach target
            while currSum >= target:
                # update res
                res = min(res, right - left + 1)
                # update currSum and move L
                currSum -= nums[left]
                left += 1

        return 0 if res == float("inf") else res