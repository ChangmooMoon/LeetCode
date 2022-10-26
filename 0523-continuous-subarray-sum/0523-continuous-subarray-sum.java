class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int N = nums.length;
        int[] psum = new int[N + 1];
        for(int i = 1; i <= N; ++i) {
            psum[i] = psum[i - 1] + nums[i - 1];
        }
        
        Set<Integer> set = new HashSet<>();
        for(int i = 2; i <= N; ++i) {
            set.add(psum[i - 2] % k);
            if(set.contains(psum[i] % k)) return true;
        }
        
        return false;
    }
}
