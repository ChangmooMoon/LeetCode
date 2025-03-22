class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        tree = defaultdict(set)
        for curr, next in edges:
            tree[curr].add(next)
            tree[next].add(curr)

        q = deque([(1, 0, 1)]) # curr_node, curr_time, prob
        while q:
            curr, time, prob = q.popleft()
            if curr == target:
                return prob if time == t or len(tree[curr]) == 0 else 0
            if time == t:
                continue
                
            for next in tree[curr]:
                q.append((next, time+1, prob/len(tree[curr])))
                tree[next].remove(curr)

        return 0     
"""
1. imp tree
2. calc prob dur traverse
"""