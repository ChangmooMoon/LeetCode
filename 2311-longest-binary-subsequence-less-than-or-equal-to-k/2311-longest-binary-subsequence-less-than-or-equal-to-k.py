class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        one, result, digit = 0, 0, 1
        
        for i in reversed(range(len(s))):
            if result + digit > k:
                break
            elif s[i] == '1':
                one += 1
                result += digit
            digit <<= 1
            
        return one + s.count('0')

'''
1. 바이너리 문자열 s, 양수 k
s 길이 1~1000, k 1~10억
k <= int('s2', 2) 인 가장 긴 s2 찾기
- leading zero 가능
- empty string은 0과 같음

2. 10^9니까 최대 길이 9의 substring까지 가능함
슬라이딩 윈도우로 길이 0~9까지 다 계산해본다?

1001010 -> 00010는 2, 00100는 4, 00101는 5
역방향으로 substring 만들면서 2^0 자리부터 K값 넘기전까지 서브스트링 만들어나가면서 계산함. 1이 들어가는 최고길이만 만들고 그앞에 leading zero 붙인다
'''