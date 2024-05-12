class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = int(1e9) + 7
        ans = 0
        count = Counter()

        for num in nums:
            count[num - self.reverse(num)] += 1

        for freq in count.values():
            ans += freq * (freq - 1) // 2
            ans %= MOD

        return ans
    
    def reverse(self, n):
        curr = 0
        while n:
            curr = curr * 10 + (n % 10)
            n //= 10
        return curr