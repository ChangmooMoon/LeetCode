class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans = float("inf")
        
        s_counter, t_counter = Counter(s), Counter(target)
        for ch in target:
            ans = min(ans, s_counter[ch] // t_counter[ch])
        
        return ans
        
"""
1. N = s len = 100, t len = 10
"""