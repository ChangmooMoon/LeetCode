# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid, slow.next = slow.next, None
        L = self.sortList(head)
        R = self.sortList(mid)
        
        dummy = ListNode()
        curr = dummy
        while L and R:
            if L.val < R.val:
                curr.next = L
                L = L.next
            else:
                curr.next = R
                R = R.next
            curr = curr.next
            
        curr.next = L or R
        return dummy.next
    
        
        
'''
1. single linkedlist 정렬
time O(NlogN), space O(1)

2. merge sort로 정렬
'''