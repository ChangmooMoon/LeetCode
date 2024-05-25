from heapq import heappush, heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)

        wq_ratio = [] # (proportion[i], qual[i])
        for i in range(N):
            wq_ratio.append(((wage[i] / quality[i]), quality[i]))
        wq_ratio.sort(key=lambda el: el[0])

        cost = -1
        total_qual = 0
        pick = [] # quality max_heap

        for i in range(N):
            prop, qual = wq_ratio[i]
            heappush(pick, -qual)
            total_qual += qual

            if len(pick) > k:
                total_qual -= -heappop(pick)
            
            if len(pick) == k:
                prop = wq_ratio[i][0]
                if cost == -1 or total_qual * prop < cost:
                    cost = total_qual * prop
        
        return cost
