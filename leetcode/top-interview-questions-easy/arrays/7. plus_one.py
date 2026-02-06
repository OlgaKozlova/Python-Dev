class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        shoudIncreasePrevious = False
        resultArray = []
        i = len(digits) - 1
        while i >=0:
            isLast = i == len(digits) - 1
            shouldAddOne = isLast or shouldIncreasePrevious
            current = digits[i]
            result = current + 1 if shouldAddOne else current
            digitResult = result % 10
            resultArray.insert(0, digitResult)
            shouldIncreasePrevious = result > 9
            i -= 1
        
        if shouldIncreasePrevious:
            resultArray.insert(0, 1)
        
        return resultArray
