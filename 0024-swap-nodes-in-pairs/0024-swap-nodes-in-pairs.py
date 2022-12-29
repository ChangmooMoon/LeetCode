# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            # 포인터 저장
            nextPair = curr.next.next # 포인터 저장
            second = curr.next
             
            # 페어를 뒤집음
            second.next = curr
            curr.next = nextPair
            prev.next = second
            
            # 포인터 업데이트
            prev = curr
            curr = nextPair
            
        return dummy.next
        