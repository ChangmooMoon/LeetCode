class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        d = [0] * (len(s) + 1)

        for l, r, dir in shifts:
            d[l] += -1 if dir else 1
            d[r + 1] += 1 if dir else -1
        
        diff = 0
        char_int = [ord(ch) - ord('a') for ch in s]
        for i in reversed(range(len(s) + 1)):
            diff += d[i]
            char_int[i - 1] = (diff + char_int[i - 1] + 26) % 26
        
        s = [chr(ord('a') + n) for n in char_int]
        return "".join(s)
