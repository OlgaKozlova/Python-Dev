# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currentNode = head #1a
    
        while currentNode is not None:
            nextNode = currentNode.next # сохраняем хвост
            currentNode.next = prevNode # разворот
            prevNode = currentNode # смещаем раз
            currentNode = nextNode # смещаем два
        
        return prevNode
        
        