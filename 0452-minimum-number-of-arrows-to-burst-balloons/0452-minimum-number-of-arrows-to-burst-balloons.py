class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort() # always next st is greater or equal to prev st

        ret = 1
        st, en = points[0]
        for next_st, next_en in points[1:]:
            if next_st > en:
                ret += 1
                st, en = next_st, next_en
            else:
                en = min(en, next_en)
        
        return ret
