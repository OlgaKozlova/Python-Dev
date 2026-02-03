class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = {}
        for char in s:
            count = map.get(char, 0)
            # Ну эта задача уже легче пошла переписываться
            # Но когда есть get но нет set - это оригинально
            map[char] = count + 1
            
        for char in t:
            count = map.get(char, 0)
            map[char] = count - 1
            
        for key in map.values():
            if key != 0:
                return False
            
        return True
        
       