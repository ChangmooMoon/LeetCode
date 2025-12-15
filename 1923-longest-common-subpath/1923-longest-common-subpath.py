class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        MOD1, MOD2 = 10**11 + 19, 10**11 + 7
        BASE1, BASE2 = 911382323, 972663749

        min_len = min(len(p) for p in paths)

        pow1 = [1] * (min_len + 1)
        pow2 = [1] * (min_len + 1)
        for i in range(1, min_len + 1):
            pow1[i] = (pow1[i - 1] * BASE1) % MOD1
            pow2[i] = (pow2[i - 1] * BASE2) % MOD2

        def check(L: int) -> bool:
            if L == 0:
                return True

            common = None

            for path in paths:
                h1 = h2 = 0
                curr_hashes = set()

                for i in range(L):
                    h1 = (h1 * BASE1 + (path[i] + 1)) % MOD1
                    h2 = (h2 * BASE2 + (path[i] + 1)) % MOD2
                curr_hashes.add((h1, h2))

                for i in range(L, len(path)):
                    out_val = path[i - L] + 1
                    in_val = path[i] + 1

                    h1 = (h1 - out_val * pow1[L - 1]) % MOD1
                    h2 = (h2 - out_val * pow2[L - 1]) % MOD2

                    h1 = (h1 * BASE1 + in_val) % MOD1
                    h2 = (h2 * BASE2 + in_val) % MOD2

                    curr_hashes.add((h1, h2))

                if common is None:
                    common = curr_hashes
                else:
                    common &= curr_hashes

                if not common:
                    return False

            return bool(common)

        lo, hi = 0, min_len
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans