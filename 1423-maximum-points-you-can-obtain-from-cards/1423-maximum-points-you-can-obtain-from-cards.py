class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        psum = sum(cardPoints[:k])
        maxSum = psum
        
        for i in range(1, k + 1):
            psum = psum - cardPoints[k - i] + cardPoints[-i] # i기준으로 왼쪽 빼고 오른쪽 더한다
            maxSum = max(maxSum, psum)
            
        return maxSum
    
'''
1. cardPoints 가 주어짐. k개 앞뒤로 뺐을 때 얻을 수 있는 최대합

2. 앞뒤로 뺀다는거는 이후 케이스에 영향을 미친다는 뜻
a 길이 10만
'''