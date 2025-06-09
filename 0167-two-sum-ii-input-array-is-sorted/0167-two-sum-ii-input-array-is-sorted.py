class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            res = numbers[l] + numbers[r]
            if res == target:
                break
            if target < res:
                r -= 1
            elif target > res:
                l += 1
        
        return [l+1, r+1]
