class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        _, prev_en = intervals[0]
        ans = 0
        
        for st, en in intervals[1:]:
            if prev_en <= st:
                prev_en = en
            else: # 겹치는 경우
                ans += 1
                prev_en = min(prev_en, en) # 진행방향을 덜 가리는 선분 선택
                
        return ans
        
"""
1. 간격이 주어질 때 안 겹치게 만드는 최소 삭제 횟수
n 10만, nlogn
st, en -5만~5만

2. 정렬 후 그리디로 접근?
짧은 거 먼저 배치하고, 긴거 배치할 떄 겹치면 뺀다로 접근해보자
투포인터로 접근
"""