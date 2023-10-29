class RangeModule:

    def __init__(self):
        self.a = []

    def addRange(self, left: int, right: int) -> None:
        bisect.insort(self.a, [left, right])
        
        res = [self.a[0]]
        
        for i in range(len(self.a)):
            interval = self.a[i]
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
                
        self.a = res

    def queryRange(self, left: int, right: int) -> bool:
        idx = bisect.bisect(self.a, [left, int(1e9)])
        
        if not self.a or idx == 0:
            return False
    
        return self.a[idx - 1][1] >= right
        

    def removeRange(self, left: int, right: int) -> None:
        res = []
        
        # no overlap, interval < range, LR overlap, range < interval
        for interval in self.a:
            if left <= interval[0] and interval[1] <= right: 
                continue
            elif interval[1] <= left or right <= interval[0]:
                res.append(interval)
            elif left < interval[0]:
                res.append([right, interval[1]])
            elif right > interval[1]:
                res.append([interval[0], left])
            else:
                res.append([interval[0], left])
                res.append([right, interval[1]])
                
        self.a = res
                


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

"""
1. left <= x < right, 1~1e9
less than O(N) -> logN, sorted range, binary range search

"""