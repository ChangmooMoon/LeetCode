class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        
        for i in range(len(items1)):
            v, w = items1[i][0], items1[i][1]
            d[v] = w
        
        for i in range(len(items2)):
            v, w = items2[i][0], items2[i][1]
            d[v] += w
            
        return sorted([[k, v] for k, v in d.items()])
        