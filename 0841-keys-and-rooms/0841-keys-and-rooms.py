class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        is_open = [True] + [False] * (N - 1)

        q = deque(rooms[0])
        while q:
            key = q.popleft()
            if not is_open[key]:
                is_open[key] = True
                q.extend(rooms[key])

        return all(is_open)
