class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        accum = 0
        for num in nums:
            accum = accum ^ num
        return accum
