from game1 import *

class PlayWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 450))
        pygame.display.set_caption("Выбор игры")

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

            self.GREEN = (0, 200, 0)
            self.screen.fill(self.GREEN)
            background = pygame.image.load(os.path.join('data', 'game_data', 'fon.jpg'))
            self.screen.blit(background, (0, 0))
            kamina_button.draw(self.screen)
            simon_button.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

    def open_game_window_kamina(self):
        # Отображение игры Камина
        pass

    def open_game_window_simon(self):
        # Отображение игры Симон
        simon_game = MemoryGame()
        simon_game.start_game()


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 255)
        self.text = text

    def draw(self, screen):
        button_surface = pygame.Surface((self.rect.width, self.rect.height),
                                        pygame.SRCALPHA)
        pygame.draw.rect(button_surface, (*self.color, 128), button_surface.get_rect(),
                         border_radius=20)
        font = pygame.font.SysFont('Impact', 30)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=button_surface.get_rect().center)
        button_surface.blit(text, text_rect)
        screen.blit(button_surface, self.rect)  # Отображение поверхности с кнопкой на экране

    def is_over(self, pos):
        return self.rect.collidepoint(pos)


# Создаем кнопки
kamina_button = Button(100, 80, 200, 100, "Камина")
simon_button = Button(100, 190, 200, 100, "Симон")
