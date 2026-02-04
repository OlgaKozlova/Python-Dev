class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            started = s[start]
            ended = s[end]
            while start < end and not started.isalnum():
                start+=1
                started=s[start]
            
            while start < end and not ended.isalnum():
                end-=1
                ended = s[end]
            
            if started.lower() != ended.lower():
                return False
            
            start+=1
            end-=1
        return True