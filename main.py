import pygame
import sys
import os
import random
from playwin import *
from abtwin import *

class GameLauncher:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.GREEN = (0, 200, 0)
        self.size = self.WIDTH, self.HEIGHT = 800, 450
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Anime Solitaire: Memes & Gosling')
        cursor_img = pygame.image.load(os.path.join('data', 'arrow.png'))

        self.font = pygame.font.Font('data/MP Manga.ttf', 30)

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
            background = pygame.image.load(os.path.join('data', 'game_data', 'fon2.jpg'))
            self.screen.blit(background, (0, 0))
            self.draw_text()
            self.draw_buttons()
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.screen.blit(cursor_img, (x, y))
            pygame.mouse.set_visible(False)
            pygame.display.flip()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def draw_text(self):
        text_surface = self.font.render('Играйте с удовольствием!', True, (255, 20, 147))
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 70))
        self.screen.blit(text_surface, text_rect)

    def draw_buttons(self):
        button_spacing = 70
        button_width = 250
        button_height = 50
        play_button_text = self.font.render('Играть', True, (255, 255, 255))
        play_button_surface = pygame.Surface((button_width, button_height),
                                             pygame.SRCALPHA)
        pygame.draw.rect(play_button_surface, (242, 185, 224, 200), play_button_surface.get_rect(),
                         border_radius=20)
        self.play_button_rect = pygame.Rect(self.WIDTH // 2 - button_width // 2, 150, button_width, button_height)
        self.screen.blit(play_button_surface,
                         (self.WIDTH // 2 - button_width // 2, 150))
        self.screen.blit(play_button_text, (self.WIDTH // 2 - play_button_text.get_width() // 2, 160))

        stats_button_text = self.font.render('Статистика', True, (255, 255, 255))
        stats_button_surface = pygame.Surface((button_width, button_height),
                                              pygame.SRCALPHA)  # Создание поверхности с альфа-каналом
        pygame.draw.rect(stats_button_surface, (242, 185, 224, 200), stats_button_surface.get_rect(),
                         border_radius=20)  # Заполнение поверхности цветом с альфа-каналом
        self.stats_button_rect = pygame.Rect(self.WIDTH // 2 - button_width // 2, 150 + button_spacing, button_width,
                                             button_height)
        self.screen.blit(stats_button_surface, (
        self.WIDTH // 2 - button_width // 2, 150 + button_spacing))  # Отображение поверхности с кнопкой на экране
        self.screen.blit(stats_button_text,
                         (self.WIDTH // 2 - stats_button_text.get_width() // 2, 160 + button_spacing))

        about_button_text = self.font.render('Об игре', True, (255, 255, 255))
        about_button_surface = pygame.Surface((button_width, button_height),
                                              pygame.SRCALPHA)  # Создание поверхности с альфа-каналом
        pygame.draw.rect(about_button_surface, (242, 185, 224, 200), about_button_surface.get_rect(),
                         border_radius=20)  # Заполнение поверхности цветом с альфа-каналом
        self.about_button_rect = pygame.Rect(self.WIDTH // 2 - button_width // 2, 150 + button_spacing * 2,
                                             button_width, button_height)
        self.screen.blit(about_button_surface, (
        self.WIDTH // 2 - button_width // 2, 150 + button_spacing * 2))  # Отображение поверхности с кнопкой на экране
        self.screen.blit(about_button_text,
                         (self.WIDTH // 2 - about_button_text.get_width() // 2, 160 + button_spacing * 2))

    def show_play_window(self):
        play_window = PlayWindow()
        play_window.show_window()

    def show_statistics_window(self):
        stats_window = StatsWindow()
        stats_window.show_window()

    def show_about_window(self):
        about_window = AboutWindow(self.screen)
        about_window.show_window()


class StatsWindow:
    def show_window(self):
        pass



GameLauncher()
