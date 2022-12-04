class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        return bf(0, 0, nums, target);
    }
    
    int bf(int idx, int sum, int[] nums, int target) {
        if(idx == nums.length) {
            return sum == target ? 1 : 0;
        }
        
        return bf(idx + 1, sum + nums[idx], nums, target)
            + bf(idx + 1, sum - nums[idx], nums, target);
    }
}