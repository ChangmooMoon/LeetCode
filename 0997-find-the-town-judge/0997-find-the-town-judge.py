class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        
        ind, outd = [0] * (n + 1), [0] * (n + 1)
        
        for st, en in trust:
            ind[en] +=  1
            outd[st] += 1
            
        for i in range(1, n + 1):
            if ind[i] == n - 1 and not outd[i]:
                return i
        
        return -1