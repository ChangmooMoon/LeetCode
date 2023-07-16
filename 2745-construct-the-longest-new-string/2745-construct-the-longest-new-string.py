class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if (x == y):
            return 4 * y + 2 * z
        return 4 * min(x, y) + 2 + 2 * z
        
'''
1. x, y, z가 있는데 "AA" "BB" "AB" 사용가능 횟수
AAA BBB 포함되면 안되게 하면서 제일 긴 문자열 만들기

2. 
AA - BB
BB - (AA or AB)
AB - (AA or AB)

x = 2, y = 1
AA BB AA 2*2 + 2 * 1
x = 1, y = 2
BB AA BB 2*1 + 2*2
x = 1 y = 2 z = 1
BB AA BB AB 2*1 + 2*2 + 2 * 1

'''