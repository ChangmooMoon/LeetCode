class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total_water = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                
                dist = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                total_water += dist * waters
            stack.append(i)
        return total_water