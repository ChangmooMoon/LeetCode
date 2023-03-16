class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 0x3f3f3f3f
        
        d = [inf] * 10001
        d[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                d[j] = min(d[j], d[j - coins[i]] + 1)
        
        return -1 if d[amount] == inf else d[amount]
        
        
'''
1. coin 배열이 주어짐. 다른 단위
최소갯수 동전으로 amount를 만들어야됨. 조합이 없으면 -1 리턴

코인 12가지, coin[i] 21억, amount 1만
'''