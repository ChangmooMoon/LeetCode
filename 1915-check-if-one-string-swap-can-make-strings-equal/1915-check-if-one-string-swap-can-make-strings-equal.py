class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: 
            return True
        
        diff_ind = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diff_ind) != 2:
            return False

        i, j = diff_ind
        return s1[i] == s2[j] and s1[j] == s2[i]
        