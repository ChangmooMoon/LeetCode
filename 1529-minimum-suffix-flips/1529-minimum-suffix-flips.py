class Solution:
    def minFlips(self, target: str) -> int:
        cnt = 0
        flip = False

        for ch in target:
            if ch != '0' and not flip:
                flip = True
                cnt += 1
            elif ch == '0' and flip:
                flip = False
                cnt += 1
        
        return cnt
