
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if map.get(num):
                return True
            else:
                map[num] = True
        return False
