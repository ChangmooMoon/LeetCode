class Solution:
    def balancedString(self, s: str) -> int:
        cntr = Counter(s)
        target = len(s) // 4
        excess = {ch: max(0, cntr[ch] - target) for ch in 'QWER'}
        if all(v == 0 for v in excess.values()):
            return 0
        
        left = 0
        min_len = len(s)
        for right in range(len(s)):
            cntr[s[right]] -= 1
            while all(cntr[ch] <= target for ch in 'QWER'):
                min_len = min(min_len, right - left + 1)
                cntr[s[left]] += 1
                left += 1
        return min_len
