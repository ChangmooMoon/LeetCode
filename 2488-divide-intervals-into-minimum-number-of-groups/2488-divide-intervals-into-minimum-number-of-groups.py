from heapq import heappush, heappop

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        h = []

        for l, r in sorted(intervals):
            if h and h[0] < l:
                heappop(h)
            heappush(h, r)

        return len(h)