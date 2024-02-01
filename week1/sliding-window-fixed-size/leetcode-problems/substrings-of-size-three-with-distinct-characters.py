class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        window = collections.defaultdict(int)
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1

            if right - left + 1 == 3:
                if len(window) == 3:
                    res += 1
                
                window[s[left]] -= 1
                if window[s[left]] == 0: 
                    del window[s[left]]
                left += 1
        
        return res