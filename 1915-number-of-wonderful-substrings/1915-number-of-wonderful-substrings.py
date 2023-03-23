class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counter = {0: 1}
        ans = 0
        bit = 0
        
        for ch in word:
            bit ^= 1 << (ord(ch) - ord('a'))
            for i in range(10):
                ans += counter.get(bit ^ (1 << i), 0)
            ans += counter.get(bit, 0)
            counter[bit] = counter.get(bit, 0) + 1
            
        return ans
        
                

            
    
'''
1. wonderful string 최대 1개 문자가 홀수번 출현하는 string
a~j로 이루어진 word에서 wonderful substring 갯수 찾기
word 길이 10만, a~j로 이루어짐 10개

2. N^2 안됨, 


'''