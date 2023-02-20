# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret = ListNode()
        curr = ret
        
        while True:
            minVal = sys.maxsize
            minIdx = -1
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                if lists[i].val < minVal:
                    minIdx = i
                    minVal = lists[i].val
            if minIdx == -1:
                break
                
            curr.next = ListNode(minVal)
            curr = curr.next
            lists[minIdx] = lists[minIdx].next
        
        return ret.next
                         
                
        
'''
1. k개의 링크드리스트로 이루어진 리스트
모든 링크드리스트는 오름차순으로 정렬.
이걸 하나의 정렬된 링크드리스트로 만들어라

2. 병합정렬로 풀자
시작노드가 몇인지 다 체크해서 포인터를 하나씩 증가시키면서 해당 값을 비교해서 끼워넣기

'''