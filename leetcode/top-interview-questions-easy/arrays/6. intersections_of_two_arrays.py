class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        result = []
        
        for num1 in nums1:
            count = map.get(num1, 0)
            map[num1] = count + 1
        
        for num2 in nums2:
            count = map.get(num2, 0)
            if not count:
                continue
            result.append(num2)
            map[num2] = count - 1
            
        return result
