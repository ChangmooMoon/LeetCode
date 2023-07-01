from bisect import *

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        N = len(nums)
        ret = []
        window = sorted(nums[:k]) # 시작 윈도우
        ret.append(self.getMedian(window, k))
        
        for i in range(1, N - k + 1):
            window.pop(bisect_left(window, nums[i - 1]))
            insort(window, nums[i + k - 1])
            ret.append(self.getMedian(window, k))
        
        return ret
            
    
    def getMedian(self, nums, k) -> float:
        if k & 1:
            return nums[k // 2]
        else:
            return (nums[k // 2] + nums[k // 2 - 1]) / 2


# 1. 윈도우 사이즈 범위에서 median 구하기, 사이즈 짝수 홀수
# 2. bisect