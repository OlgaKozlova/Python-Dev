# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else None
            #print(slow.val if slow is not None else slow, fast.val if fast is not None else fast)
        
        reverse_start = slow if fast is None else slow.next
        
        prev = None
        reverse_head = reverse_start
        while reverse_head is not None:
            next_node = reverse_head.next
            reverse_head.next = prev
            prev = reverse_head
            reverse_head = next_node
           
        
        last = prev
        first = head
        while last is not None:
            if last.val != first.val:
                return False
            else:
                last = last.next
                first = first.next
        
        return True
