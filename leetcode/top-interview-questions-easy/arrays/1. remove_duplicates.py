class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        startIndex = 0
        for i in range(len(nums)):
            if nums[i] > nums[startIndex]:
                startIndex += 1
                nums[startIndex] = nums[i]
        
        return startIndex + 1
        

