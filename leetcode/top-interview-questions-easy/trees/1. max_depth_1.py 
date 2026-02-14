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
        
        nodes = [[root]]
        i = 0
        while i < len(nodes):
            subnodes = nodes[i]
            next_subnodes = []
            
            for subnode in subnodes:
                if subnode.left is not None:
                    next_subnodes.append(subnode.left)
                if subnode.right is not None:
                    next_subnodes.append(subnode.right)
                
            if len(next_subnodes) > 0:
                nodes.append(next_subnodes)
            
            print(len(nodes))
            
            i += 1
        
        return len(nodes)
        
        
        
        