class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_move = abs(target[0]) + abs(target[1])
        min_ghost_move = min([abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) for ghost in ghosts])

        return my_move < min_ghost_move
