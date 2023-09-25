class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        logs.sort(key=lambda x: x[1])
        
        print(logs)
        
        ans_id, max_t = logs[0]
        for i in range(1, len(logs)):
            t_id, curr_time = logs[i]
            d = curr_time - logs[i - 1][1]
            
            if d > max_t:
                ans_id = t_id
                max_t = d
            elif d == max_t:
                ans_id = min(ans_id, t_id)
                
        return ans_id;
        