class Solution(object):
    def reverseString(self, s):
        leng = len(s)
        for i in range(0, leng / 2):
            lastIndex = leng - i - 1
            first = s[i]
            last = s[lastIndex]
            s[i] = last
            s[lastIndex] = first