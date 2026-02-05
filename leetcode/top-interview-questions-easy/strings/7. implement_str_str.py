class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        i = 0
        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
                j+=1
            i+=1
        return -1