class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        
        s1, s2 = set(nums1), set(nums2)
        ans.append(list(s1 - s2))
        ans.append(list(s2 - s1))
        
        return ans
        