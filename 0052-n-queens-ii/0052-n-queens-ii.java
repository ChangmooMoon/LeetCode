class Solution {
    int[] a = new int[9];
    int N, cnt = 0;
    
    public int totalNQueens(int n) {
        N = n;
        calc(0);
        return cnt;
    }
    
    void calc(int queen) {
        boolean place = false;
        if(queen == N) {
            ++cnt;
            return;
        }
        
        for(int i = 0; i < N; ++i) {
            place = true;
                
            for(int j = 0; j < queen; ++j) {
                if(a[j] == i || Math.abs(queen - j) == Math.abs(i - a[j])) {
                    place = false;
                    break;
                }
            }
            
            if(place) {
                a[queen] = i;
                calc(queen + 1);
            }
        }
    }
}