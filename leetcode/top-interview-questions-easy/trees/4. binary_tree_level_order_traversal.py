# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        self.sth(root, result, 0)
        
        return result
    
        
    def sth(self, node, result, level):
        if node is None:
            return
        
        if len(result) == level:
            result.append([node.val])
        else:
            result[level].append(node.val)
        
        self.sth(node.left, result, level + 1)
        self.sth(node.right, result, level + 1)
        