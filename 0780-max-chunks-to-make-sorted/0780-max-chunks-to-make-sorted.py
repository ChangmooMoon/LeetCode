class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans, curr = 0, 0
        for i in range(len(arr)):
            if curr < arr[i]:
                curr = arr[i]
            if curr == i:
                ans += 1
        
        return ans

'''
4 3 2 1 0
0 0 1 1 1

1 0 2 3 4
0 1 2 3 4

0 1 3 2 4
0 1 2 3 4
'''