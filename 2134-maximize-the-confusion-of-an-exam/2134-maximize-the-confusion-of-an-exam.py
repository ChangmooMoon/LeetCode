class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # k switch, the longest consecutive of T
        def go(answerKey):
            N = len(answerKey)
            curr = k
            ret = 0
            l = r = 0

            while r < N:
                if answerKey[r] == 'T':
                    pass
                elif curr > 0:
                    curr -= 1
                else:
                    while answerKey[l] == 'T':
                        l += 1
                    l += 1
                
                ret = max(ret, r - l + 1)
                r += 1
            return ret

        res = "".join(('F' if x == 'T' else 'T') for x in answerKey)
        return max(go(answerKey), go(res))