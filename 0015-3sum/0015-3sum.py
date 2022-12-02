class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
                
            L, R = i + 1, len(nums) - 1
            while(L < R):
                sum = nums[i] + nums[L] + nums[R]
                if sum < 0:
                    L += 1
                elif sum > 0:
                    R -= 1
                else:
                    ret.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1
        return ret
                        
            
            
        
    
    
# 0. 문제 읽기
# 	- 3개의 원소 합이 0인 조합 찾기, 원소의 값은 다 달라야됨
# 	- 원소의 갯수 3000. O(N^2) 이하로 풀어야됨
# 1. 논리적 순서 확정
# 	- N^2는 되니까 2중 for문으로 두개의 합을 해시에 저장해서 푼다?
# 	- 중복처리 쉽도록 정렬
# 2. 필요한 자료연산 리스트업
# - 0~N-2 범위를 순회하면서 그 안에서 L-R 투포인터로 target값 맞추기
# 3. 이에 제일 유리한 자료구조 선택
# - sort(), 투포인터
# 4. 구현
