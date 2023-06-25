class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        for key in counter:
            if counter[key] > len(arr) / 4:
                return key
            
        return -1
        