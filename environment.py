import random
from collections import deque

N = 8


class ChaseEnvironment:
    def __init__(self, size=N):
        self.size = size
        self.lion_start = (0, 0)

        while True:
            self.grid = [[' ' for _ in range(size)] for _ in range(size)]
            num_walls = 15
            placed = 0
            while placed < num_walls:
                wx, wy = random.randint(0, size - 1), random.randint(0, size - 1)
                if (wx, wy) != self.lion_start:
                    if self.grid[wy][wx] == ' ':
                        self.grid[wy][wx] = 'W'
                        placed += 1

            while True:
                dx, dy = random.randint(0, size - 1), random.randint(0, size - 1)
                if (dx, dy) != self.lion_start and self.grid[dy][dx] == ' ':
                    self.deer_start = (dx, dy)
                    break

            if self.is_reachable(self.lion_start, self.deer_start):
                break

    def is_reachable(self, start, end):
        queue = deque([start])
        visited = {start}
        while queue:
            x, y = queue.popleft()
            if (x, y) == end: return True
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if self.grid[ny][nx] != 'W' and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        return False

    def get_next_position(self, x, y, direction):
        if direction == 'Stay': return (x, y)
        nx, ny = x, y
        if direction == 'North':
            ny = max(0, y - 1)
        elif direction == 'South':
            ny = min(self.size - 1, y + 1)
        elif direction == 'East':
            nx = min(self.size - 1, x + 1)
        elif direction == 'West':
            nx = max(0, x - 1)
        if self.grid[ny][nx] == 'W': return (x, y)
        return (nx, ny)