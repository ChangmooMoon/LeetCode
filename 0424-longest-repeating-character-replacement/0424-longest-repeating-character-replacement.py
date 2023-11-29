class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        
        # sliding window
        max_freq = 0
        start = 0
        window_size = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            max_freq = max(max_freq, freq_map[s[end]])
            if end + 1 - start - max_freq > k:
                freq_map[s[start]] -= 1
                start += 1
                
            window_size = end + 1 - start
        
        return window_size


'''
ABAB -> AAAA . same letter string len is 4
AABABGBA -> AAAABGBA : 4
N = 10^5, less than NlogN
'''