# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        list1Current = list1
        list2Current = list2
        if list1.val > list2.val:
            newHead = list2
            list2Current = list2Current.next
        else:
            newHead = list1
            list1Current = list1Current.next
        
        memoryHead = newHead
        
        while list1Current is not None and list2Current is not None:
            if list1Current.val > list2Current.val:
                newHead.next = list2Current
                newHead = newHead.next
                list2Current = list2Current.next
            else:
                newHead.next = list1Current
                newHead = newHead.next
                list1Current = list1Current.next
        
        newHead.next = list1Current if list1Current is not None else list2Current

        return memoryHead
            
        