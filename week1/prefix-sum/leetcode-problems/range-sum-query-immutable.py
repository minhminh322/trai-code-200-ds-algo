class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = []
        total = 0
        for n in nums:
            total += n
            self.prefixSum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        # [-2, 0, 3, -5, 2, -1]
        #         L      R
        rightSum = self.prefixSum[right]
        leftSum = self.prefixSum[left - 1] if left > 0 else 0
        return rightSum - leftSum
