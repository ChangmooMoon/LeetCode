class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 0
        curr_capa = capacity
        for i, target in enumerate(plants):
            if target > curr_capa:
                curr_capa = capacity
                step += i * 2
            step += 1
            curr_capa -= target
        return step
