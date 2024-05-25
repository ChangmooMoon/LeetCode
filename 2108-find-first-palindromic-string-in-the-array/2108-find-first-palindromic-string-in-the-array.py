class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palin(s: str) -> bool:
            st, en = 0, len(s) - 1
            while st <= en:
                if s[st] != s[en]:
                    return False
                st, en = st + 1, en - 1
                
            return True
        
        for word in words:
            if is_palin(word):
                return word
        return ""
