class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        N = len(num_str)
        if N < k:
            return 0

        cnt = 0
        for i in range(N-k+1):
            sub_str = int(num_str[i:i+k])
            if sub_str != 0 and num % sub_str == 0:
                cnt += 1

        return cnt
