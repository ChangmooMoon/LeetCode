import java.util.*;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0) return "";
        
        Arrays.sort(strs, (a, b) -> a.length() - b.length());
        String ret = strs[0];
        
        for(int i = 1; i < strs.length; ++i) {
            int endIdx = cmp(ret, strs[i]);
            ret = ret.substring(0, endIdx);
        }
        
        return ret;
    }
    
    int cmp(String s1, String s2) {
        for(int i = 0; i < s1.length(); ++i) {
            if(s1.charAt(i) != s2.charAt(i)) return i;
        }
        
        return s1.length();
    }
}