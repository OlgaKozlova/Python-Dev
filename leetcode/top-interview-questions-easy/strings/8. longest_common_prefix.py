class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if (len(strs) == 1):
            return prefix
        
        for i in range(len(strs)):
            current = strs[i]
            newPrefix = ''
            
            limit = min(len(prefix), len(current))
            for j in range(limit):
                if current[j] == prefix[j]:
                    newPrefix += current[j]
                else:
                    break
            
            if newPrefix == "":
                return newPrefix
            
            prefix = newPrefix
        
        return prefix
        
       