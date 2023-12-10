class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ret = ""

        for ch in order:
            ret += ch * counter[ch]
            del counter[ch]
        
        for k, v in counter.items():
            ret += k * v
        
        return ret
        