class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        # d[i] = max(d[i-1]+a[i], d[i-2]+b[i])
        # d[A][i] = max(d[A][i-1]+a[i], d[B][i-2]+a[i])
        # d[B][i] = max(d[B][i-1]+b[i], d[A][i-2]+b[i])
        
        N = len(energyDrinkA)
        d = [[0]*2 for _ in range(N)]

        d[0][0] = energyDrinkA[0]
        d[0][1] = energyDrinkB[0]

        d[1][0] = max(d[0][0] + energyDrinkA[1], energyDrinkA[1])
        d[1][1] = max(d[0][1] + energyDrinkB[1], energyDrinkB[1])

        for i in range(2, N):
            d[i][0] = max(d[i - 1][0] + energyDrinkA[i], d[i - 2][1] + energyDrinkA[i])
            d[i][1] = max(d[i - 1][1] + energyDrinkB[i], d[i - 2][0] + energyDrinkB[i])

        return max(d[N - 1][0], d[N - 1][1])
