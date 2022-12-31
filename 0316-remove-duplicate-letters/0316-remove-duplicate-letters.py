class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, check, st = Counter(s), set(), deque()
        
        for ch in s:
            counter[ch] -= 1
            if ch in check:
                continue
            
            while st and ch < st[-1] and counter[st[-1]] > 0:
                check.remove(st.pop())
            st.append(ch)
            check.add(ch)
        
        return ''.join(st)