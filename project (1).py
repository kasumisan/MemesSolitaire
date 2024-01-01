import pygame
import sys
import os


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
        about_window = AboutWindow(self.screen)
        about_window.show_window()


class PlayWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Выбор сложности")

    def show_window(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Проверяем клик по кнопке
                    if kamina_button.is_over(event.pos):
                        self.open_game_window_kamina()
                    if simon_button.is_over(event.pos):
                        self.open_game_window_simon()

            self.screen.fill((255, 255, 255))
            kamina_button.draw(self.screen)
            simon_button.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

    def open_game_window_kamina(self):
        # Отображение игры Камина
        pass

    def open_game_window_simon(self):
        # Отображение игры Симон
        pass


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 128, 255)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)


play_window = PlayWindow()

# Создаем кнопки
kamina_button = Button(100, 50, 200, 100, "Камина")
simon_button = Button(100, 160, 200, 100, "Симон")


class StatsWindow:
    def show_window(self):
        pass


class AboutWindow:
    def __init__(self, screen):
        self.screen = screen
        self.GREEN = (0, 200, 0)
        self.font = pygame.font.Font(None, 25)
        self.version = "Версия игры: 0.1"
        self.developers = "Разработчики: "
        self.developers2 = "Швайкова Кира, "
        self.developers3 = "Симонова Арина"
        self.copyright = "© 2023 Все права защищены"
        self.image = pygame.image.load('data/rayan1.jpg')

    def show_window(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.GREEN)
            text_y = 100
            version_text = self.font.render(self.version, True, (255, 255, 255))
            self.screen.blit(version_text, (50, text_y))

            text_y += 50
            developers_text = self.font.render(self.developers, True, (255, 255, 255))
            self.screen.blit(developers_text, (50, text_y))

            text_y += 50
            developers_text = self.font.render(self.developers2, True, (255, 255, 255))
            self.screen.blit(developers_text, (50, text_y))

            text_y += 50
            developers_text = self.font.render(self.developers3, True, (255, 255, 255))
            self.screen.blit(developers_text, (50, text_y))

            text_y += 50
            copyright_text = self.font.render(self.copyright, True, (255, 255, 255))
            self.screen.blit(copyright_text, (50, text_y))

            image_rect = self.image.get_rect(center=(self.screen.get_width() - 100, self.screen.get_height() // 2))
            self.screen.blit(self.image, image_rect)

            pygame.display.flip()

        pygame.quit()
        sys.exit()


GameLauncher()
