class Solution {
    public boolean makesquare(int[] matchsticks) {
        int total = IntStream.of(matchsticks).sum();
        if(total % 4 != 0) return false;
        Arrays.sort(matchsticks);
        return dfs(matchsticks, matchsticks.length - 1, total / 4, 0, 0, 0, 0);
    }

    public boolean dfs(int[] matchsticks, int idx, int target, int s1, int s2, int s3, int s4)  {
        if(target == s1 && target == s2 && target == s3 && target == s4) return true;
        if(target < s1 || target < s2 || target < s3 || target < s4) return false;

        return
            dfs(matchsticks, idx - 1, target, s1 + matchsticks[idx], s2, s3, s4)
            || dfs(matchsticks, idx - 1, target, s1, s2 + matchsticks[idx], s3, s4)
            || dfs(matchsticks, idx - 1, target, s1, s2, s3 + matchsticks[idx], s4)
            || dfs(matchsticks, idx - 1, target, s1, s2, s3, s4 + matchsticks[idx]);
    }
}
