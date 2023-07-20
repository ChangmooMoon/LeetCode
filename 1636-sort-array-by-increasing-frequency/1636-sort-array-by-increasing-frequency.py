from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        sorted_c = sorted(counter.items(), key=lambda x: (x[1], -x[0]))
        
        ret = []
        for key, val in sorted_c:
            ret += [key] * val
        
        return ret
        
        
'''
1. increaing order based on the frequency of the values.
same freq, decreasing order
'''