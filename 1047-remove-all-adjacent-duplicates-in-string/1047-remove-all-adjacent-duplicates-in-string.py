class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = deque()
        for ch in s:
            if len(st) > 0 and st[-1] == ch:
                st.pop()
            else:
                st.append(ch)
                
        ret = ""
        while st:
            ret = st.pop() + ret
        return ret
            
        
'''
1. lowercase string s
붙어있는 2개의 같은 글자를 제거함
'''