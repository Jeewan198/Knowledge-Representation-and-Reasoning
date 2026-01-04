from environment import ChaseEnvironment
from mdp_solver import solve_mdp
from agents import get_actual_lion_move_distribution, get_deer_reactive_move
from pygame_visualizer import PygameVisualizer
import random

MAX_STAMINA = 100


def run_simulation(env, policy, visualizer):
    l_pos, d_pos, stamina = env.lion_start, env.deer_start, MAX_STAMINA
    for step in range(1, 1001):
        if not visualizer.running: break

        action = policy[l_pos[0], l_pos[1], d_pos[0], d_pos[1]]
        if not visualizer.update_display(l_pos, d_pos, step, action, (stamina / MAX_STAMINA) * 100):
            break

        # Lion Turn
        dist = get_actual_lion_move_distribution(action, l_pos, env)
        l_pos = random.choices(list(dist.keys()), weights=list(dist.values()), k=1)[0]
        stamina -= 1

        if l_pos == d_pos:
          # Update display one last time to show them in the same block
            visualizer.update_display(l_pos, d_pos, step, "CATCH!", 0)
            visualizer.show_winner_screen("LION WINS!!!", win=True)
            return
        if stamina <= 0:
            visualizer.show_winner_screen("DEER SURVIVED!", win=False)
            return

        # Deer Turn
        d_pos = get_deer_reactive_move(l_pos, d_pos, env)
        if l_pos == d_pos:
            # FIX: Update display one last time to show them in the same block
            visualizer.update_display(l_pos, d_pos, step, "CATCH!", (stamina / MAX_STAMINA) * 100)
            visualizer.show_winner_screen("LION WINS!!!", win=True)
            return


if __name__ == "__main__":
    env = ChaseEnvironment()
    print("Calculating Optimal Pursuit Policy...")
    _, policy = solve_mdp(env)
    visualizer = PygameVisualizer(env)
    run_simulation(env, policy, visualizer)