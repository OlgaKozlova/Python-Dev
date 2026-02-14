# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        current_layer = [root]
        
        
        while (not self.isEmptyLayer(current_layer)):
            if not self.isLayerSymmetric(current_layer):
                return False
            
            current_layer = self.getNextLayer(current_layer)
            #self.printLayer(current_layer)
        
        return True
        
    def isLayerSymmetric(self, layer):
        i = 0
        layer_len = len(layer)
        while i < layer_len // 2:
            if not self.isNodeEqual(layer[i], layer[layer_len - i - 1]):
                return False
            i += 1
        return True
    
    def getNextLayer(self, layer):
        result = []
        for item in layer:
            result.append(item.left if item is not None else None)
            result.append(item.right if item is not None else None)
        return result
    
    def isEmptyLayer(self, layer):
        return all (x is None for x in layer)
    
    def printLayer(self, layer):
        for i in layer:
            print(i.val if i is not None  else None)
        print()
        
    def isNodeEqual(self, one, two):
        if one is None or two is None:
            return one is two
        return one.val == two.val
        
        
        
        