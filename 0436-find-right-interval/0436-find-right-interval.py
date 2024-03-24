class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        ans = [-1] * N

        for idx, l in enumerate(intervals):
            l.append(idx)

        intervals.sort()
        for st, en, idx in intervals:
            j = bisect_left(intervals, [en])
            if j < N:
                ans[idx] = intervals[j][2]
        
        return ans