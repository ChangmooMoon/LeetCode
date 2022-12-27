# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        
        L, R = 0, len(values) - 1
        while L <= R:
            if values[L] != values[R]:
                return False
            L += 1
            R -= 1
        
        return True
            
            