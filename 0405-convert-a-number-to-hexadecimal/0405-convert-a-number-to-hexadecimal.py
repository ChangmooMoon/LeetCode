class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = False
        if num < 0:
            num = num * -1 -1
            neg = True
        
        hex_str = "0123456789abcdef"
        ans = []
        for i in range(8):
            num, r = divmod(num, 16)
            if neg:
                ans.append(hex_str[15-r])
            else:
                ans.append(hex_str[r])
        
        ans.reverse()
        return "".join(ans).lstrip("0")

# 26 -> 1a
# -1 -> ffff ffff