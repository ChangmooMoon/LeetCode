class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        pair = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for ch in s:
            if ch not in pair:
                st.append(ch)
            elif not st or pair[ch] is not st.pop():
                    return False
        
        return len(st) is 0
                    
            
