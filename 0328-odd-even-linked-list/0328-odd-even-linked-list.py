# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(-1), ListNode(-1)
        odd_head, even_head = odd, even
        
        p = 0
        while head:
            p += 1
            if p & 1:
                odd.next = ListNode(head.val)
                odd = odd.next
            else:
                even.next = ListNode(head.val)
                even = even.next
            head = head.next
        
        odd.next = even_head.next
        return odd_head.next

            
        
        
        
        
'''
1. singlely linkedList
{odd} -> {even}
'''