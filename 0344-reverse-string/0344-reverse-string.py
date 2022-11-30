class Solution:
    def reverseString(self, s: List[str]) -> None:
        st, en = 0, len(s) - 1
        while st < en:
            s[st], s[en] = s[en], s[st]
            st += 1
            en -= 1
            
        