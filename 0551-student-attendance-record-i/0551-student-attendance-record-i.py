class Solution:
    def checkRecord(self, s: str) -> bool:
        absent, late = 0, 0
        for ch in s:
            if ch == 'L':
                late += 1
            elif ch == 'A':
                absent += 1
                late = 0
            elif ch == 'P':
                late = 0
        
            if absent == 2 or late == 3:
                return False
            
        return True
                
            
                
            
        
        
        
        
        
"""
1. n 1000, A L P
- fewer than 2 day total
- fewer than 3 late consecutive
"""