import sys
sys.set_int_max_str_digits(0)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        digit, curr = 1, 0
        
        for n in num[::-1]:
            curr += n * digit
            digit *= 10
        
        return map(int, list(str(curr + k)))