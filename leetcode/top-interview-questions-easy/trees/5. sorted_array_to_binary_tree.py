# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Не идеально, зато сама
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        if (len(nums) == 0):
            return None
        
        middle = len(nums) // 2
        val = nums[middle]
        left = nums[: middle]
        right = nums[middle + 1:]
        
        return TreeNode(val, self.sortedArrayToBST(left), self.sortedArrayToBST(right))
        
        