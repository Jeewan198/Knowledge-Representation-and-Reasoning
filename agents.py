import random

DIRECTIONS = ['North', 'South', 'East', 'West', 'Stay']


def get_actual_lion_move_distribution(action, current_pos, env):
    x, y = current_pos
    dist = {}
    slip_map = {
        'North': [('North', 0.95), ('West', 0.025), ('East', 0.025)],
        'South': [('South', 0.95), ('East', 0.025), ('West', 0.025)],
        'East': [('East', 0.95), ('North', 0.025), ('South', 0.025)],
        'West': [('West', 0.95), ('South', 0.025), ('North', 0.025)],
        'Stay': [('Stay', 1.0)]
    }
    for move_dir, prob in slip_map.get(action, [('Stay', 1.0)]):
        next_pos = env.get_next_position(x, y, move_dir)
        dist[next_pos] = dist.get(next_pos, 0.0) + prob
    return dist


def get_deer_reactive_move(lion_pos, deer_pos, env):
    best_move, max_score = deer_pos, -float('inf')
    center = env.size / 2
    curr_dist_sq = (deer_pos[0] - lion_pos[0]) ** 2 + (deer_pos[1] - lion_pos[1]) ** 2

    for move1 in DIRECTIONS:
        pos1 = env.get_next_position(deer_pos[0], deer_pos[1], move1)
        best_future_score = -float('inf')
        for move2 in DIRECTIONS:
            pos2 = env.get_next_position(pos1[0], pos1[1], move2)
            dist_lion = (pos2[0] - lion_pos[0]) ** 2 + (pos2[1] - lion_pos[1]) ** 2

            weight = 4.5 if curr_dist_sq < 16 else 1.5
            dist_center_sq = (pos2[0] - center) ** 2 + (pos2[1] - center) ** 2

            score = (dist_lion * weight) - (dist_center_sq * 0.4)
            if score > best_future_score:
                best_future_score = score

        if best_future_score > max_score:
            max_score = best_future_score
            best_move = pos1
    return best_move