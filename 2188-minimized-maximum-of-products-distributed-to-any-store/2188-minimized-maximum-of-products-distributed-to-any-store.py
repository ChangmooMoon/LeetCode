class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)

        def is_poss(k):
            req = 0
            for i in quantities:
                req += math.ceil(i/k)
                if req > n:
                    return False
            return req <= n

        while l < r:
            mid = (l + r) // 2
            if is_poss(mid):
                r = mid
            else:
                l = mid + 1
        
        return l