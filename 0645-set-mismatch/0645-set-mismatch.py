class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums) # 1 to N
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        ans = [0, 0]
        for i in range(1, N + 1):
            if d[i] == 2:
                ans[0] = i
            elif d[i] == 0:
                ans[1] = i
                
        return ans
        