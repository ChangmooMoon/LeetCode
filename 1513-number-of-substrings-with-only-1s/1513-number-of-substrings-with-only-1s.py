class Solution:
    def numSub(self, s: str) -> int:
        d = [0] * 100001
        for i in range(1, 100001):
            d[i] = d[i - 1] + i
            
        a = []
        seq = 0
        for ch in s:
            if ch == '1':
                seq += 1
            elif ch == '0' and seq > 0:
                a.append(seq)
                seq = 0
        if seq > 0:
            a.append(seq)
        
        ans = 0
        for num in a:
            ans += d[num]
        
        return ans % (10 ** 9 + 7)
                
                    
        
'''
1. 바이너리 문자열 s가 주어짐
1로만 이루어진 모든 substring의 갯수 10**9 + 7로 modular 연산
s.length 10만

2. 10만^2 = 100억 O(N^2) 미만으로 풀어야
- 길이가 1~10만인 모든 바이너리 문자열에 대해서 포함된 substring의 갯수를 계산하고
- 포함된 substring 그룹의 갯수를 세서 다 더한다, modular 연산
'''