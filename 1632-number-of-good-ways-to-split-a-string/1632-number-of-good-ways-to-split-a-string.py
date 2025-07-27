class Solution:
    def numSplits(self, s: str) -> int:
        ctr = Counter(s)
        visited = set()
        ans = 0

        for ch in s:
            visited.add(ch)
            ctr[ch] -= 1
            if ctr[ch] == 0:
                ctr.pop(ch)
            ans += len(visited) == len(ctr)
        return ans
    
# 1. aacaba 
# 2. N 10^5
# a:4 b:1 c:1
# a acaba 1 3
# aa caba 1 3
# aac aba 2 2
# aaca ba 2 2
# aacab a 3 1
