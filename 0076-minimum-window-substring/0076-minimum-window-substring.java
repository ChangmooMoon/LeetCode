import java.util.*;

class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        for(char ch: t.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        
        int i = 0, j = 0, cnt = map.size(); // 범위ij, 남은 알파벳갯수cnt
        int left = 0, right = s.length() - 1, min = s.length();
        boolean found = false;
        
        while(j < s.length()) {
            char endChar = s.charAt(j++);
            if(map.containsKey(endChar)) {
                map.put(endChar, map.get(endChar) - 1);
                if(map.get(endChar) == 0) --cnt;
            }
            
            if(cnt > 0) continue;
            
            while(cnt == 0) {
                char stChar = s.charAt(i++);
                if(map.containsKey(stChar)) {
                    map.put(stChar, map.get(stChar) + 1);
                    if(map.get(stChar) > 0) ++cnt;
                }
            }
            
            if(j - i < min) {
                left = i;
                right = j;
                min = j - i;
                found = true;
            }
        }
        
        return !found ? "" : s.substring(left - 1, right);
    }
}