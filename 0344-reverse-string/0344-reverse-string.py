class Solution:
    def reverseString(self, s: List[str]) -> None:
        st, en = 0, len(s) - 1
        while st <= en:
            tmp = s[st]
            s[st] = s[en]
            s[en] = tmp
            st += 1
            en -= 1
            