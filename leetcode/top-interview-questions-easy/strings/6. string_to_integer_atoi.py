class Solution:
    def myAtoi(self, s: str) -> int:
        startParsing = False
        isNegative = False
        limit = 2 ** 31
        min = -1 * limit
        max = limit - 1
        space = ' '
        plus = '+'
        minus = '-'
        zero = '0'
        nine = '9'
        
        result = 0
        
        for char in s:
            if char == space:
                if not startParsing:
                    continue
                else:
                    break
            
            if char == plus or char == minus:
                if not startParsing:
                    startParsing = True
                    if char == minus:
                        isNegative = True
                    continue
                else:
                    break
            
            if char >= zero and char <= nine:
                number = ord(char) - ord(zero)
                startParsing = True
                result = result * 10
                result += number
                
                if isNegative:
                    if result * -1 < min:
                        return min
                elif result > max:
                        return max
            else:
                break
                    
        return result * -1 if isNegative else result

        