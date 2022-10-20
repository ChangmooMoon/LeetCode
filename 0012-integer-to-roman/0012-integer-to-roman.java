import java.util.*;

class Solution {
    public String intToRoman(int num) {
        Map<Integer, String> map = new HashMap<>(){{
            put(1, "I");
            put(5, "V");
            put(10, "X");
            put(50, "L");
            put(100, "C");
            put(500, "D");
            put(1000, "M");
        }};
        String ans = "";
        
        int place = 1;
        while(num > 0) {
            int digit = num % 10;
            String ret;
            if(digit < 4) ret = map.get(place).repeat(digit);
            else if(digit == 4) ret = map.get(place) + map.get(place * 5);
            else if(digit == 9) ret = map.get(place) + map.get(place * 10);
            else ret = map.get(place * 5) + map.get(place).repeat(digit - 5);
            
            ans = ret + ans;
            num /= 10;
            place *= 10;
        }
        
        return ans;
    }
}