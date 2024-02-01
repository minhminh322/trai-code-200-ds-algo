class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        # prefix Dict where key -> prefixSum and value -> freq
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        # Track of current PrefixSum
        currSum = 0
        # Iterate through nums
        for n in nums:
            currSum += n
            # check if currSum - k in the Dict
            if currSum - k in prefix:
                # True -> get the freq
                res += prefix[currSum - k]
            # Add currSum to dict
            prefix[currSum] += 1
            
        return res

        