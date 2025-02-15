class Solution:
    def reformat(self, s: str) -> str:
        l, d = [], []
        for ch in s:
            l.append(ch) if ch.isdigit() else d.append(ch)
        if abs(len(l) - len(d)) > 1:
            return ""
        if len(l) < len(d):
            l, d = d, l # always len l 

        ans = []
        for i in range(len(d)):
            ans.append(l[i])
            ans.append(d[i])

        if len(l) > len(d):
            ans.append(l[-1])
        
        return "".join(ans)
