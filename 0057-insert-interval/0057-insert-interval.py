class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        N = len(intervals)
        new_st, new_en = newInterval[0], newInterval[1]
        
        while i < N and intervals[i][1] < new_st: # en < new_st
            ans.append(intervals[i])
            i += 1
        
        while i < N and intervals[i][0] <= new_en: # st <= new_en
            new_st = min(new_st, intervals[i][0])
            new_en = max(new_en, intervals[i][1])
            i += 1
        
        ans.append([new_st, new_en])
        
        while i < N:
            ans.append(intervals[i])
            i += 1
        
        return ans
                
                
        
                
                
        
        
'''
1. invervals 들이 안겹치게 주어짐
st 순으로 오름차순 정렬되어있는데, 
new interval 들어가도 no overlapping되게 정렬. 겹치면 merge
N 1만, st, en 0~10^5

2. 10만개 d로 선언해서 dfs
겹치는 경우, 안겹치는 경우
- 겹치는 경우
- 안 겹치고 왼쪽, 오른쪽에 있는 경우
    - 왼쪽에 있는 경우
    - 오른쪽에 있는 경우
'''