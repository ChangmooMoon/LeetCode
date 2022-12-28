# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)
    
    def reverse(self, forward: ListNode, backward: ListNode = None):
        if forward is None:
           return backward

        next_forward = forward.next
        forward.next = backward
        return self.reverse(next_forward, forward)