class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # fi, se <-> se, fi
        def psum(fi, se):
            n = len(nums)
            d = [0] * (n + 1)
            for i in range(n):
                d[i+1] = d[i] + nums[i]
            
            max_d, res = 0, 0
            for i in range(fi + se, n + 1):
                max_d = max(max_d, d[i-se]-d[i-se-fi]) # fi
                res = max(res, max_d+d[i]-d[i-se])
            return res
        
        return max(psum(firstLen, secondLen), psum(secondLen, firstLen))