class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        notNullIndex = 0
        for i in range(len(nums)):
            current = nums[i]
            if current != 0:
                nums[i] = nums[notNullIndex]
                nums[notNullIndex] = current
                notNullIndex += 1
       