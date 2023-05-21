class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day, ret  = {}, 0
        
        for t in tasks:
            ret = max(day.get(t, 0), ret + 1)
            day[t] = ret + space + 1
            
        return ret