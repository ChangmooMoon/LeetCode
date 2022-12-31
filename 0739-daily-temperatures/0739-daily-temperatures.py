class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        st = deque()
        
        for i, val in enumerate(T):
            while st and val > T[st[-1]]: # 스택이 비거나, 직전보다 낮은 온도가 나올 때까지 반복
                last = st.pop()
                ans[last] = i - last
            st.append(i)
        
        return ans
