class Solution {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        int[][] a = new int[n][2];
        for(int i = 0; i < n; ++i) {
            a[i] = new int[] {speed[i], efficiency[i]};
        }
        
        Arrays.sort(a, (p1, p2) -> p2[1] - p1[1]);
        
        long speedSum = 0, ret = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int[] el: a) {
            pq.add(el[0]);
            speedSum += el[0];
            if(pq.size() > k) speedSum -= pq.poll();
            ret = Math.max(ret, speedSum * el[1]);
        }
        
        return (int)(ret % (long)(1e9 + 7));
    }
}