class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        
        def count_one(num):
            cnt = 0
            while num:
                cnt += num & 1
                num >>= 1
            return cnt
        
        for i in range(n + 1):
            ret.append(count_one(i))
        
        return ret