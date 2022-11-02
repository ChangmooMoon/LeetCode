class Solution {
    public int snakesAndLadders(int[][] board) {
        int N = board.length;
        int[] a = new int[401];
        
        boolean goRight = true;
        int p = 1;
        for(int i = N - 1; i >= 0; --i) {
            if(goRight) {
                for(int j = 0; j < N; ++j) {
                    a[p++] = board[i][j];
                }
            } else {
                for(int j = N - 1; j >= 0; --j) {
                    a[p++] = board[i][j];
                }
            }
            goRight = !goRight;
        }
        
        return bfs(a, N);
    }
    
    static int bfs(int[] a, int N) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[401];
        
        q.add(1);
        visited[1] = true;
        
        int step = 0;
        while(!q.isEmpty()) {
            int size = q.size();
            for(int i = 0; i < size; ++i) {
                int curr = q.poll();
                if(curr == N * N) return step;
                
                for(int next = curr + 1; next <= Math.min(curr + 6, N * N); ++next) {
                    int realNext = a[next] == -1 ? next: a[next];
                    if(visited[realNext]) continue;    
                    
                    visited[realNext] = true;
                    q.add(realNext);
                }
            }
            
            ++step;
        }
        
        return -1;
    }
}