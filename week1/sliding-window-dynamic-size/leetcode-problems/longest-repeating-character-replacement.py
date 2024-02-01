class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # freq dict
        freq = dict()
        res = 0
        left = 0
        # iterate through string
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            # shrink until windowSize - mostFreq <= k
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            # Update result
            res = max(res, right - left + 1)
        return res
