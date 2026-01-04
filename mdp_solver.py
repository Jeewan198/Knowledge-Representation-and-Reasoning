import numpy as np
from environment import N


def solve_mdp(env, gamma=0.9, epsilon=0.1):
    V = np.zeros((N, N, N, N))
    policy = np.full((N, N, N, N), 'Stay', dtype=object)
    walls = np.zeros((N, N), dtype=bool)
    for y in range(N):
        for x in range(N):
            if env.grid[y][x] == 'W': walls[y][x] = True

    for _ in range(50):
        new_V = np.copy(V)
        for lx in range(N):
            for ly in range(N):
                if walls[ly][lx]: continue
                for dx in range(N):
                    for dy in range(N):
                        if walls[dy][dx] or (lx == dx and ly == dy): continue
                        best_val = -float('inf')
                        for action in ['North', 'South', 'East', 'West']:
                            nx, ny = lx, ly
                            if action == 'North':
                                ny = max(0, ly - 1)
                            elif action == 'South':
                                ny = min(N - 1, ly + 1)
                            elif action == 'East':
                                nx = min(N - 1, lx + 1)
                            elif action == 'West':
                                nx = max(0, lx - 1)
                            if walls[ny][nx]: nx, ny = lx, ly

                            reward = 1000 if (nx == dx and ny == dy) else -1
                            val = reward + gamma * V[nx, ny, dx, dy]
                            if val > best_val:
                                best_val = val
                                policy[lx, ly, dx, dy] = action
                        new_V[lx, ly, dx, dy] = best_val
        if np.max(np.abs(new_V - V)) < epsilon: break
        V = new_V
    return V, policy