import pygame
import os
from game1 import MemoryGame
from game2 import Play


class PlayWindow:
    def __init__(self):
        pygame.init()
        self.size = self.WIDTH, self.HEIGHT = 800, 450
        self.screen = pygame.display.set_mode(self.size)
        self.cursor_img = pygame.image.load(os.path.join('data', 'arrow.png'))

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
                    if back_button.is_over(event.pos):
                        from main import GameLauncher
                        gamelau = GameLauncher()
                        gamelau.run()

            self.GREEN = (0, 200, 0)
            self.font = pygame.font.Font('data/MP Manga.ttf', 50)
            self.screen.fill(self.GREEN)
            background = pygame.image.load(os.path.join('data', 'game_data', 'fon3.jpg'))
            self.screen.blit(background, (0, 0))
            kamina_button.draw(self.screen)
            simon_button.draw(self.screen)
            back_button.draw(self.screen)
            self.draw_text()
            pygame.mouse.set_visible(False)
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.screen.blit(self.cursor_img, (x, y))

            pygame.display.flip()

        pygame.quit()

    def open_game_window_kamina(self):
        # Отображение игры Камина
        kamina_game = MemoryGame()
        kamina_game.start_game()

    def open_game_window_simon(self):
        simon_game = Play()
        simon_game.run()

    def draw_text(self):
        text_surface = self.font.render('Вы котик?', True, (242, 185, 224))
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 70))
        self.screen.blit(text_surface, text_rect)
        text_surface1 = self.font.render('Да', True, (242, 185, 224))
        text_rect1 = text_surface1.get_rect(center=(200, 260))
        self.screen.blit(text_surface1, text_rect1)
        text_surface2 = self.font.render('Нет', True, (242, 185, 224))
        text_rect2 = text_surface2.get_rect(center=(600, 260))
        self.screen.blit(text_surface2, text_rect2)


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (242, 185, 224)
        self.text = text

    def draw(self, screen):
        button_surface = pygame.Surface((self.rect.width, self.rect.height),
                                        pygame.SRCALPHA)
        pygame.draw.rect(button_surface, (*self.color, 250), button_surface.get_rect(),
                         border_radius=50)
        font = pygame.font.Font('data/MP Manga.ttf', 20)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=button_surface.get_rect().center)
        button_surface.blit(text, text_rect)
        screen.blit(button_surface, self.rect)  # Отображение поверхности с кнопкой на экране

    def is_over(self, pos):
        return self.rect.collidepoint(pos)


# Создаем кнопки
kamina_button = Button(75, 300, 250, 50, "Покушаем и спать")
simon_button = Button(475, 300, 250, 50, "Кисдуем на работу!")
back_button = Button(275, 370, 250, 50, 'Назад')
