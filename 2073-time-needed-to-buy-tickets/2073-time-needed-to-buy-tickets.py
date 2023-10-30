class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        q = deque()
        for i, v in enumerate(tickets):
            q.append((v, True)) if i == k else q.append((v, False))
                
        while True:
            val, is_target = q.popleft()
            time += 1
            val -= 1
            if not val:
                if is_target:
                    break
            else:
                q.append((val, is_target))
        
        return time
