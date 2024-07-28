class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def getCost(target): 
            # a <= c <= b, cost = abs(a - c) * x + abs(b - c) * y
            return sum(abs(nums[i] - target) * cost[i] for i in range(len(nums)))
            
        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            cost1 = getCost(mid)
            cost2 = getCost(mid + 1)
            if cost1 < cost2:
                hi = mid
            else:
                lo = mid + 1

        return getCost(lo)