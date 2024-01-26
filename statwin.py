import pygame
import sqlite3
import os

class GameResultsWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Результаты")
        self.font = pygame.font.Font('data/MP Manga.ttf', 25)
        self.game_data = self.load_game_data()
        self.game_results = self.load_game_results()
        self.back_button_color = (255, 255, 255)
        self.back_button_rect = pygame.Rect(50, self.screen.get_height() - 70, 150, 50)
        self.back_button_text = 'Назад'
        self.back_button_text_surface = self.font.render(self.back_button_text, True, (0, 0, 0))

    def load_game_data(self):
        conn = sqlite3.connect("game_data.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS results (play_time REAL, date TEXT)")
        cursor.execute("SELECT * FROM results")
        data = cursor.fetchall()
        conn.close()
        return data

    def load_game_results(self):
        conn = sqlite3.connect("game_results.db")
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS game_result (score INTEGER, elapsed_time INTEGER)')
        cursor.execute("SELECT * FROM game_result")
        data = cursor.fetchall()
        conn.close()
        return data

    def render_text(self, text, x, y):
        surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(surface, (x, y))

    def run(self):
        running = True
        cursor_img = pygame.image.load(os.path.join('data', 'arrow.png'))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.back_button_rect.collidepoint(mouse_pos):
                        from main import GameLauncher
                        gamel = GameLauncher()
                        gamel.run()
            background = pygame.image.load(os.path.join('data', 'game_data', 'fon5.jpg'))
            self.screen.blit(background, (0, 0))
            self.render_text("Платформер:", 50, 50)
            self.render_text("Пасьянс:", 600, 50)
            self.render_text('Время', 50, 100)
            self.render_text('Дата', 150, 100)
            self.render_text('Очки', 600, 100)
            y = 150
            for row in self.game_data:
                for i, value in enumerate(row):
                    self.render_text(str(value), 50 + i * 100, y)
                y += 30

            y = 150
            for row in self.game_results:
                for i, value in enumerate(row):
                    self.render_text(str(value), 600 + i * 100, y)
                y += 30
            pygame.draw.rect(self.screen, self.back_button_color, self.back_button_rect, border_radius=20)
            back_text_rect = self.back_button_text_surface.get_rect(center=self.back_button_rect.center)
            self.screen.blit(self.back_button_text_surface, back_text_rect)
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.screen.blit(cursor_img, (x, y))
            pygame.mouse.set_visible(False)
            pygame.display.flip()
        pygame.quit()
