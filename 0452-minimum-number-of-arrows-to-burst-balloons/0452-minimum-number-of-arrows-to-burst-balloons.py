class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))

        ret = 1
        en = points[0][1]
        for next_st, next_en in points[1:]:
            if next_st > en:
                ret += 1
                en = next_en
        
        return ret
