class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        counter = counter.most_common()
        
        N = len(arr)
        elCnt = N
        cnt = 0
        
        for i in range(len(counter)):
            cnt += 1
            elCnt -= counter[i][1]
            if elCnt <= N // 2:
                break
        
        return cnt