class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()
        for ch in s:
            if ch.isdigit():
                nums.add(int(ch))

        if len(nums) < 2:
            return -1
        
        return heapq.nlargest(2, nums)[1]
