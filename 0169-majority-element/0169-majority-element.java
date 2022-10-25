class Solution {
    public int majorityElement(int[] nums) {
        int cnt = 0, ret = 0x3f3f3f3f;
        
        for(int n: nums) {
            if(cnt == 0) ret = n;
            cnt += (n == ret) ? 1 : -1;
        }
        
        return ret;
    }
}
