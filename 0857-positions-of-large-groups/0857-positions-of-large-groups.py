class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        
        st = 0
        for i in range(len(s)):
            if s[i] == s[st]:
                continue
            if i - st >= 3:
                ans.append([st, i - 1])
            st = i

        if len(s) - st >= 3:
            ans.append([st, len(s) - 1])
             
        return ans