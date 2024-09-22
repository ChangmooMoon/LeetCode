class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        ans = [0]
        for arr in mat:
            ans = sorted(fi + se for fi in ans for se in arr[:k])[:k]
        
        return ans[-1]
