class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        pairs = sorted(zip(scores, ages))
        d = [pairs[i][0] for i in range(N)]
        
        for i in range(N): # pairs[i] = (score, age)
            for j in range(i):
                if pairs[i][1] >= pairs[j][1]:
                    d[i] = max(d[i], pairs[i][0] + d[j])
        
        return max(d)
        

        
        
'''
1. 농구팀이 있는데 토너먼트를 함. the score of the team이 최대이도록 해야됨
conflicts가 생기면 안됨. 어린선수가 늙은선수보다 더 많이 득점하면 안됨. 같은 나이이면 conflict 발생 안함
score, age로 ith 선수 정보, 팀이 득점할 수 있는 최대값
N 1~1000 N^2 = 100만


2. 
- 같은 나이끼리는 점수 차이나도 됨
- 낮은 나이 선수가 나이 많은 선수보다 더 많은 점수를 내면 안됨
나이순으로 정렬해서 어린선수가 더 많이 득점하면 픽하지 않는다
각 나이의 최소득점자보다 적게 득점한다? 밑에 나이대 선수들이 더 많이 득점하면?
dfs는 O 2^N은 안됨, 
subproblem으로 쪼개서 접근 N^2

d[i] = i 지점까지 도달했을때 팀점수 최대값
d[i] = max(d[i], d[j] + 추가할수 있는 선수점수)
d[i] = max(d[i], d[j] + pairs[i][0]), i < j
'''