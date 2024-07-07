class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)

        s = set()
        for i in range(N):
            for j in range(i + 1, N):
                s.add((arr[i] / arr[j], arr[i], arr[j]))
        
        s = list(s)
        s.sort()
        return [s[k - 1][1], s[k - 1][2]]
        