class Solution {
    public boolean stoneGame(int[] piles) {
        int N = piles.length;
        int[][] d = new int[N][N];
        
        for(int i = 0; i < N; ++i) {
            d[i][i] = piles[i];
        }
        
        for(int len = 2; len <= N; ++len) {
            for(int i = 0; i < N; ++i) {
                int j = i + len - 1;
                if(j >= N) continue;
                
                d[i][j] = Math.max(piles[i] - d[i + 1][j], piles[j] - d[i][j - 1]);
            }
        }
        
        return d[0][N - 1] > 0;
    }
}

// d[i][j] = max(a[i] - d[i + 1], a[i] - d[i][j -1])