import java.util.*;

class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if(a[0] == b[0]) return b[1] - a[1];
            return a[0] - b[0];
        });
        
        int s = intervals[0][0];
        int e = intervals[0][1];
        int del = 0;

        for(int i = 1; i < intervals.length; ++i) {
            if(s <= intervals[i][0] && intervals[i][1] <= e) ++del;
            else {
                s = intervals[i][0];
                e = intervals[i][1];
            }
        }
        
        return intervals.length - del;
    }
}