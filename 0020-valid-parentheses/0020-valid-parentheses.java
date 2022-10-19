import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        Map<Character, Character> parse = new HashMap<>() {{
            put(')', '(');
            put(']', '[');
            put('}', '{');
        }};
        
        for(char ch: s.toCharArray()) {
            if(ch == '(' || ch == '[' || ch == '{') st.push(ch);
            else {
                if(st.empty() || st.peek() != parse.get(ch)) return false;
                st.pop();
            }
        }
        
        return st.empty();
    }
}