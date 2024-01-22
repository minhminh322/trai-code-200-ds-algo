class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res, currSum = 0, 0
        left = 0
        window = collections.defaultdict(int)

        for right in range(len(nums)):
            currSum += nums[right]
            window[nums[right]] += 1

            if right - left + 1 == k:
                if len(window.keys()) == k:
                    res = max(res, currSum)

                currSum -= nums[left]
                window[nums[left]] -= 1

                if window[nums[left]] == 0: window.pop(nums[left])
                left += 1
        
        return res