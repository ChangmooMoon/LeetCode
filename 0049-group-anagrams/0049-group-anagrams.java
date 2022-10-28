class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List> map = new HashMap<>();
        
        for(String s: strs) {
            char[] chArr = s.toCharArray();
            Arrays.sort(chArr);
            
            String key = String.valueOf(chArr);
            if(!map.containsKey(key)) map.put(key, new ArrayList());
            map.get(key).add(s);
        }
        
        return new ArrayList(map.values());
    }
}
