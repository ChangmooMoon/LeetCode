class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ret = ""
        maxh = []
        
        for cnt, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(maxh, (cnt, ch))
        
        while maxh:
            cnt, ch = heapq.heappop(maxh)
            
            if len(ret) > 1 and ret[-1] == ret[-2] == ch:
                if not maxh:
                    break
                cnt2, ch2 = heapq.heappop(maxh)
                ret += ch2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(maxh, (cnt2, ch2))
            else:
                ret += ch
                cnt += 1
                
            if cnt:
                heapq.heappush(maxh, (cnt, ch))
                
        return ret