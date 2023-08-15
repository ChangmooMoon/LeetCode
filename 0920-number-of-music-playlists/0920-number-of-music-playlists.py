class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        
        d = [[0] * (n + 1) for _ in range(goal + 1)]
        
        d[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                d[i][j] = d[i - 1][j - 1] * (n - (j - 1)) # 새 노래 추가
                if j - k > 0:
                    d[i][j] += d[i - 1][j] * (j - k) # 기존 노래 추가 가능한 경우
                    d[i][j] %= MOD
                    
        return d[goal][n]

"""
1. 음악 N개 중에 goal개 선택, 중복가능, 최소 한번은 다 들어야됨, 
다른 노래가 k번 이상 재생되면 그때부터 중복선택 가능
n, goal, k 0~100, k < n <= goal

2. d[i][j] = 길이 i이고 j개의 노래종류 포함된 playlist 갯수

새 노래 추가하는 경우 or 기존 노래 추가하는 경우(기존 픽한 j개 노래종류에서 중복선택)
d[i][j] = d[i - 1][j - 1] * (n - (j - 1)) + d[i - 1][j] * (j - k)

d[i][j] = d[i - 1][j - 1] * (n - (j - 1))
d[i][j] = d[i - 1][j - 1] * (n - (j - 1)) + d[i - 1][j] * (j - k)
"""