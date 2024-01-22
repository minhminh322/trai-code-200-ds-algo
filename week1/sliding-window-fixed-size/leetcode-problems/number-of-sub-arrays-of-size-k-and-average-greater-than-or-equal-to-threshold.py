class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        left = 0
        currSum = 0
        for right in range(len(arr)):
            # Open window
            currSum += arr[right]

            if right - left + 1 == k:
                if (currSum / k) >= threshold:
                    ans += 1
                
                # Close window
                currSum -= arr[left]
                left += 1

        return ans