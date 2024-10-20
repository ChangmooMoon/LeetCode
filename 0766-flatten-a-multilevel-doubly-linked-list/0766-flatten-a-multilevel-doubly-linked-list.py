"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return head

        dummy_front = Node(-1)
        curr = dummy_front
        st = [head]
        while st:
            cand = st.pop()
            if cand.next: 
                st.append(cand.next)
            if cand.child: 
                st.append(cand.child)

            curr.next = cand # curr -> cand
            cand.prev = curr
            cand.child = None
            curr = cand

        dummy_front.next.prev = None
        return dummy_front.next

        



            


