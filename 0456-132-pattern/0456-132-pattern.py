class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False
        
        th = -0x3f3f3f3f
        
        st = []
        for num in nums[::-1]:
            if num < th:
                return True
            
            while st and st[-1] < num:
                th = st.pop()
            st.append(num)
        
        return False
            
            
        
        
        
'''
1. 132 패턴이 있는지 여부
i < j < k 이고, a[i] < a[k] < a[j]
N 20만

2. 20만개니까 슬라이딩 윈도우로 계속 검사하면서 전진하다가 발견되면 리턴?
i < j 이면서 j < k인 모든 경우의 수를 다 검사해야됨. N^2이라 안됨

2. 모노토닉 스택? 배열을 역순으로 순회하면서 스택에 담고 스택은 내림차순 정렬을 유지함. 현재 위치보다 오른쪽에 있는 값 중 가장 작은 값보다 큰 값을 찾는다?


'''