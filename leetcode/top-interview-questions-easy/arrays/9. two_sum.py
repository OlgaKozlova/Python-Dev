class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            current = nums[i]
            need = target - current
            needIndex = seen.get(need, None)
            if needIndex is not None:
                return [needIndex, i]
            else:
                seen[current] = i