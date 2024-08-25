class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToInt(s):
            h, m = int(s[0:2]), int(s[3:])
            return h * 60 + m
        
        times = []
        for t in timePoints:
            times.append(timeToInt(t))
            times.append(timeToInt(t) + 1440)
        times.sort()

        ans = 1440 # 60 * 24
        for i in range(len(times) - 1):
            ans = min(ans, times[i + 1] - times[i])

        return ans
        