from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        return self.dfs(freq)
    
    def dfs(self, freq):
        if sum(freq.values()) <= 0:
            return 0
        
        ret = 0
        for key in freq.keys():
            if not freq[key]:
                continue
                
            freq[key] -= 1
            ret += self.dfs(freq) + 1
            freq[key] += 1
        
        return ret
            
        
        
        
        
'''
1. tiles로 만들 수 있는 모든 str 조합
'''