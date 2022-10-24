import java.util.*;

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int lo = 0, hi = arr.length - 1;
        
        while(hi - lo >= k) {
            int diff1 = Math.abs(arr[lo] - x);
            int diff2 = Math.abs(arr[hi] - x);
            if(diff1 > diff2) ++lo;
            else --hi;
        }
        
        List<Integer> ans = new ArrayList<>();
        for(int i = lo; i <= hi; ++i) {
            ans.add(arr[i]);
        }
        
        return ans;
    }
}