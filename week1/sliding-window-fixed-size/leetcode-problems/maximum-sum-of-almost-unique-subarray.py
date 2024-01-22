class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res, currSum = 0, 0
        left = 0
        window = collections.defaultdict(int)

        for right in range(len(nums)):
            # Expand the window
            currSum += nums[right]
            window[nums[right]] += 1

            # Meet the threashold
            if right - left + 1 == k:
                # Process the current window
                if len(window.keys()) >= m:
                    res = max(res, currSum)

                # Shrink the window
                currSum -= nums[left]
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    window.pop(nums[left])
                left += 1

        return res