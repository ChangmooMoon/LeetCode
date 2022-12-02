class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i - 1 >= 0 and nums[i - 1] == nums[i]: # 중복처리
                continue
                
            L, R = i + 1, len(nums) - 1
            while(L < R):
                sum = nums[i] + nums[L] + nums[R]
                if sum < 0:
                    L += 1
                elif sum > 0:
                    R -= 1
                else:
                    ret.append([nums[i], nums[L], nums[R]]) # 정답
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return ret

    # [-2 -2 0 2 2]
