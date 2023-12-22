import pygame
import sys


class GameLauncher:
    def __init__(self):
        pygame.init()

        self.GREEN = (0, 200, 0)

        self.size = self.WIDTH, self.HEIGHT = 400, 400
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Anime Solitaire: Memes & Gosling')

        self.font = pygame.font.Font(None, 30)

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.play_button_rect.collidepoint(pos):
                        self.show_play_window()
                    elif self.stats_button_rect.collidepoint(pos):
                        self.show_statistics_window()
                    elif self.about_button_rect.collidepoint(pos):
                        self.show_about_window()

            self.screen.fill(self.GREEN)
            self.draw_text()
            self.draw_buttons()
            pygame.display.flip()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def draw_text(self):
        text_surface = self.font.render('Играйте с удовольствием!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 50))
        self.screen.blit(text_surface, text_rect)

    def draw_buttons(self):
        button_spacing = 50
        button_width = 200
        button_height = 40
        play_button_text = self.font.render('Играть', True, (0, 0, 0))
        self.play_button_rect = pygame.Rect(self.WIDTH // 2 - button_width // 2, 150, button_width, button_height)
        pygame.draw.rect(self.screen, (255, 255, 255), self.play_button_rect)
        self.screen.blit(play_button_text, (self.WIDTH // 2 - play_button_text.get_width() // 2, 155))

        stats_button_text = self.font.render('Статистика', True, (0, 0, 0))
        self.stats_button_rect = pygame.Rect(self.WIDTH // 2 - button_width // 2, 150 + button_spacing, button_width,
                                             button_height)
        pygame.draw.rect(self.screen, (255, 255, 255), self.stats_button_rect)
        self.screen.blit(stats_button_text,
                         (self.WIDTH // 2 - stats_button_text.get_width() // 2, 155 + button_spacing))

        about_button_text = self.font.render('Об игре', True, (0, 0, 0))
        self.about_button_rect = pygame.Rect(self.WIDTH // 2 - button_width // 2, 150 + button_spacing * 2,
                                             button_width, button_height)
        pygame.draw.rect(self.screen, (255, 255, 255), self.about_button_rect)
        self.screen.blit(about_button_text,
                         (self.WIDTH // 2 - about_button_text.get_width() // 2, 155 + button_spacing * 2))

    def show_play_window(self):
        play_window = PlayWindow()
        play_window.show_window()

    def show_statistics_window(self):
        stats_window = StatsWindow()
        stats_window.show_window()

    def show_about_window(self):
        about_window = AboutWindow()
        about_window.show_window()


class PlayWindow:
    def show_window(self):
        pass


class StatsWindow:
    def show_window(self):
        pass


class AboutWindow:
    def show_window(self):
        pass


GameLauncher()
