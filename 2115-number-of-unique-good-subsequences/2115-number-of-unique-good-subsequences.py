class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9+7
        N = len(binary)
        st = 0

        while st < N and binary[st] == '0': # leading zero
            st += 1
        
        if st == N:
            return 1
        
        d = [0] * N
        d[st] = 1
        last_0 = last_1 = 0

        for i in range(st+1, N):
            j = last_0 if binary[i] == '0' else last_1
            nd = d[j - 1] if j > 0 else 0
            d[i] = d[i - 1] * 2 - nd

            if binary[i] == '0':
                last_0 = i
            else:
                last_1 = i
        
        cnt_0 = 1 if '0' in binary else 0
        return (d[-1] + cnt_0) % MOD
