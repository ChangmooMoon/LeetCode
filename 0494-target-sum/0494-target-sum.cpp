class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        return bf(0, 0, nums, target);
    }
    
    int bf(int idx, int sum, vector<int>& nums, int target) {
        if(idx == nums.size()) {
            return sum == target;
        }
        
        return bf(idx + 1, sum + nums[idx], nums, target)
            + bf(idx + 1, sum - nums[idx], nums, target);
    }
};
