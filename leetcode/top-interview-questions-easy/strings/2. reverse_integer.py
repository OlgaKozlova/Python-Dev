class Solution(object):
    def reverse(self, x):
        isNegative = x < 0
        str_x = str(x)
        
        if (isNegative):
            str_x = str_x[1:]
            
        arr_x = list(str_x)
        # сложно менять js паттерны, в js я делаю "sdf".split('')
        arr_x.reverse()
        str_x = "".join(arr_x)
        
        str_x = str_x.lstrip('0')
        # Но тут конечно круто что без тупых регулярок можно
        if (len(str_x) == 0):
            return 0
        
        if (len(str_x) > 10):
            return 0
        
        if (len(str_x) == 10):
            compare = '2147483648' if isNegative else '2147483647'
            # В питоне нет тернарников ААА как с этим жить
            if (str_x > compare):
                return 0
            
        return int(str_x) * (-1 if isNegative else 1)
