import java.util.*;

class Solution {
    public int romanToInt(String s) {
        int ret = 0;
        for(int i = 0; i < s.length(); ++i) {
            char ch = s.charAt(i);
            if(ch == 'I') {
                if(s.indexOf("IV", i) == i) {
                    ret += 4;
                    ++i;
                } else if(s.indexOf("IX") == i) {
                    ret += 9;
                    ++i;
                } else ret += 1;
            } else if(ch == 'V') {
                ret += 5;
            } else if(ch == 'X') {
                if(s.indexOf("XL", i) == i) {
                    ret += 40;
                    ++i;
                } else if(s.indexOf("XC", i) == i) {
                    ret += 90;
                    ++i;
                } else ret += 10;
            } else if(ch == 'L') {
                ret += 50;
            } else if(ch == 'C') {
                if(s.indexOf("CD", i) == i) {
                    ret += 400;
                    ++i;
                } else if(s.indexOf("CM", i) == i) {
                    ret += 900;
                    ++i;
                } else ret += 100;
            } else if(ch == 'D') {
                ret += 500;
            } else if(ch == 'M') {
                ret += 1000;
            }
        }
        
        return ret;
    }
}