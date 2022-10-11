class Solution {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        int[][] a = new int[n][2];
        for(int i = 0; i < n; ++i) {
            a[i][0] = speed[i];
            a[i][1] = efficiency[i];
        }
        
        Arrays.sort(a, (p1, p2) -> p2[1] - p1[1]);
        
        long speedSum = 0;
        long ret = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < n; ++i) {
            while(pq.size() >= k) speedSum -= pq.remove();
            
            pq.add(a[i][0]);
            speedSum += a[i][0];
            ret = Math.max(speedSum * a[i][1], ret);
        }
        
        return (int)(ret % ((int)1e9 + 7));
    }
}