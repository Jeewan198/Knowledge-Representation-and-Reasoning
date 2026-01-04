import pygame

CELL_SIZE, FPS, UI_HEIGHT = 60, 2, 80
BG_COLOR, GRID_COLOR, UI_COLOR = (144, 238, 144), (100, 160, 100), (40, 40, 40)


class PygameVisualizer:
    def __init__(self, env):
        self.env = env
        pygame.init()
        self.grid_dim = self.env.size * CELL_SIZE
        self.screen = pygame.display.set_mode((self.grid_dim, self.grid_dim + UI_HEIGHT))
        pygame.display.set_caption("Lion vs Deer: KRR Project")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 28)
        self.big_font = pygame.font.Font(None, 50)
        self.running, self.images = True, {}
        for name, file in [('lion', 'lion.png'), ('deer', 'deer.png'), ('tree', 'tree.png'), ('rock', 'rock.png')]:
            try:
                img = pygame.image.load(file).convert_alpha()
                self.images[name] = pygame.transform.scale(img, (int(CELL_SIZE * 0.8), int(CELL_SIZE * 0.8)))
            except:
                self.images[name] = None

    def update_display(self, l_pos, d_pos, step, action, stamina_pct):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False
        self.screen.fill(BG_COLOR)
        for y in range(self.env.size):
            for x in range(self.env.size):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GRID_COLOR, rect, 1)
                if self.env.grid[y][x] == 'W':
                    img = self.images['tree'] if (x + y) % 2 == 0 else self.images['rock']
                    if img: self.screen.blit(img, (x * CELL_SIZE + 6, y * CELL_SIZE + 6))

        self.screen.blit(self.images['deer'], (d_pos[0] * CELL_SIZE + 6, d_pos[1] * CELL_SIZE + 6))
        self.screen.blit(self.images['lion'], (l_pos[0] * CELL_SIZE + 6, l_pos[1] * CELL_SIZE + 6))

        pygame.draw.rect(self.screen, UI_COLOR, (0, self.grid_dim, self.grid_dim, UI_HEIGHT))
        txt = self.font.render(f"Step: {step} | Lion Move: {action}", True, (255, 255, 255))
        self.screen.blit(txt, (15, self.grid_dim + 15))
        pygame.draw.rect(self.screen, (60, 20, 20), (15, self.grid_dim + 45, self.grid_dim - 30, 15))
        color = (0, 255, 0) if stamina_pct > 30 else (255, 0, 0)
        pygame.draw.rect(self.screen, color,
                         (15, self.grid_dim + 45, int((stamina_pct / 100) * (self.grid_dim - 30)), 15))
        pygame.display.flip()
        self.clock.tick(FPS)
        return self.running

    def show_winner_screen(self, winner_text, win=True):
        overlay = pygame.Surface((self.grid_dim, self.grid_dim + UI_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start < 4000:
            self.screen.blit(overlay, (0, 0))
            color = (255, 215, 0) if win else (100, 255, 100)
            msg = self.big_font.render(winner_text, True, color)
            self.screen.blit(msg, msg.get_rect(center=(self.grid_dim // 2, (self.grid_dim + UI_HEIGHT) // 2)))
            pygame.display.flip()
            pygame.time.delay(30)