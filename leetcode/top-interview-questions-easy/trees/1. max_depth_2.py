from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        nodes = deque([root])
        i = 0
        while nodes:
            level_size = len(nodes)
            for _ in range(level_size):
                node = nodes.popleft()
                if (node.left):
                    nodes.append(node.left)
                if (node.right):
                    nodes.append(node.right)
                
            i += 1
        
        return i
        
        
        
        