import pygame
import sqlite3

class GameResultsWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Game Results")
        self.font = pygame.font.Font(None, 30)
        self.game_data = self.load_game_data()
        self.game_results = self.load_game_results()

    def load_game_data(self):
        conn = sqlite3.connect("game_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results")
        data = cursor.fetchall()
        conn.close()
        return data

    def load_game_results(self):
        conn = sqlite3.connect("game_results.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM game_result")
        data = cursor.fetchall()
        conn.close()
        return data

    def render_text(self, text, x, y):
        surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(surface, (x, y))

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            self.render_text("Game Data:", 50, 50)
            self.render_text("Game Results:", 600, 50)

            y = 100
            for row in self.game_data:
                for i, value in enumerate(row):
                    self.render_text(str(value), 50 + i * 100, y)
                y += 30

            y = 100
            for row in self.game_results:
                for i, value in enumerate(row):
                    self.render_text(str(value), 600 + i * 100, y)
                y += 30

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

if __name__ == "__main__":
    window = GameResultsWindow()
    window.run()
