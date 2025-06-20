class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        l, r = 0, N-1

        # find postfix idx -> ans = N-1-l or r-1-l or N-1 or 0
        while 0 < r and arr[r-1] <= arr[r]:
            r -= 1
        ans = r

        # find prefix idx
        while l < r:
            while r < N and arr[l] > arr[r]:
                r += 1
            ans = min(ans, r-1-l)
            if arr[l] > arr[l+1]:
                break
            l += 1

        return ans

# less than ON^2 
# [1,2,3,10,4,2,3,5]
# [1,2,3,       3,5]