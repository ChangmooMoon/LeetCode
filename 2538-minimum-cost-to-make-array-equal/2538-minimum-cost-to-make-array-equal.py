class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def getCost(target): 
            # a <= c <= b, cost = abs(a - c) * x + abs(b - c) * y
            return sum(abs(nums[i] - target) * cost[i] for i in range(len(nums)))

        N = len(nums)
        if N == 1:
            return 0

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid1 = lo + (hi - lo) // 3
            mid2 = hi - (hi - lo) // 3
            cost1 = getCost(mid1)
            cost2 = getCost(mid2)
            if cost1 < cost2:
                hi = mid2 - 1
            else:
                lo = mid1 + 1

        return getCost(lo)
            