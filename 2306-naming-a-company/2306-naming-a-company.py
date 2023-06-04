class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        setArr = [set() for _ in range(26)]
        for idea in ideas:
            setArr[ord(idea[0]) - ord('a')].add(idea[1:])
        
        ans = 0
        for i in range(25):
            for j in range(i + 1, 26):
                ret = len(setArr[i] & setArr[j]) # 중복되는 suffix 갯수
                ans += 2 * (len(setArr[i]) - ret) * (len(setArr[j]) - ret)
        
        return ans