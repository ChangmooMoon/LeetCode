# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        pIdx = 0
        while p:
            p = p.next
            pIdx += 1
        
        target = pIdx // 2
        
        while target:
            head = head.next
            target -= 1
            
        return head
