# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            tmp, tmp.next, slow = slow, tmp, slow.next
            
        if fast:
            slow = slow.next
            
        while tmp and tmp.val == slow.val:
            slow, tmp = slow.next, tmp.next
        return not tmp
        