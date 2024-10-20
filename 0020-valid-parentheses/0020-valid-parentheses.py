class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        paren = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for ch in s:
            if ch not in paren:
                st.append(ch)
            elif not(st and paren[ch] == st.pop()):
                return False
        
        return len(st) == 0