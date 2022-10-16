import java.util.*;

class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>() {{
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};
        
        int ret = 0;
        for(int i = 0; i < s.length(); ++i) {
            int val = map.get(s.charAt(i));
            if(i + 1 < s.length() && map.get(s.charAt(i + 1)) > val) {
                ret -= val;
            } else ret += val;
        }
        
        return ret;
    }
}