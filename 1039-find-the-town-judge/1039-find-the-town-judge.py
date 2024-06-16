class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        
        if not trust:
            return -1
        
        ind = [set() for _ in range(n + 1)]
        for t in trust:
            a, b = t[0], t[1]
            ind[b].add(a)
            
        judge_cand = -1
        for idx, s in enumerate(ind):
            if len(s) == n - 1:
                judge_cand = idx
        
        if judge_cand == -1:
            return -1

        for s in ind:
            if judge_cand in s:
                return -1
        
        return judge_cand