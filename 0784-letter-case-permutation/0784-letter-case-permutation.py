class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = [""]
        
        for ch in s:
            tmp = []
            if ch.isalpha(): # 대문자, 소문자 추가
                for rest in ret:
                    tmp.append(rest + ch.lower())
                    tmp.append(rest + ch.upper())
            else:
                for rest in ret:
                    tmp.append(rest + ch)
            ret = tmp
        
        return ret