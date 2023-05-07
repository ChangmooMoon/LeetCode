class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        prev, next = [], []
        sameCnt = 0
        
        for n in nums:
            if n < pivot:
                prev.append(n)
            elif n > pivot:
                next.append(n)
            else:
                sameCnt += 1
        
        return prev + [pivot] * sameCnt + next
        
        
        