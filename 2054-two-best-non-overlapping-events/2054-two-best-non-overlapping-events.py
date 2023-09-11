class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        timeline = []
        for st, en, val in events:
            timeline.append((st, 1, val)) # start
            timeline.append((en + 1, -1, val)) # end
        
        timeline.sort() 
        
        curr_val, ans = 0, 0
        for _, type, val in timeline: # time, start or end, val
            if type == 1:
                ans = max(ans, curr_val + val)
            else:
                curr_val = max(curr_val, val)
                
        return ans
        
"""
1. events[i] = [st, en, val], at most 2 nonoverlapping events, maximize value
value is positive, pick 1 or 2 events, len = 10^5

2. 
- pick 1
- pick 2
time range is too big. need a compression
"""