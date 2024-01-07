from main import *

class AboutWindow:
    def __init__(self, screen):
        self.screen = screen
        self.GREEN = (0, 200, 0)
        self.font = pygame.font.Font('Mikar.ttf', 20)
        self.version = "Версия игры: 0.1"
        self.developers = "Разработчики: "
        self.developers2 = "Швайкова Кира, "
        self.developers3 = "Симонова Арина"
        self.copyright = "© 2023 Все права защищены"
        self.image = pygame.image.load('data/rayan1.jpg')
        self.back_button_color = (255, 255, 255)
        self.back_button_rect = pygame.Rect(50, self.screen.get_height() - 70, 100, 50)
        self.back_button_text = 'Назад'
        self.back_button_text_surface = self.font.render(self.back_button_text, True, (0, 0, 0))

    def show_window(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.back_button_rect.collidepoint(mouse_pos):
                        GameLauncher()
                        running = False

            self.screen.fill(self.GREEN)
            background = pygame.image.load(os.path.join('data', 'game_data', 'fon.jpg'))
            self.screen.blit(background, (0, 0))
            text_y = 70
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

            image_rect = self.image.get_rect(center=(self.screen.get_width() - 100, self.screen.get_height() // 2.5))
            self.screen.blit(self.image, image_rect)

            pygame.draw.rect(self.screen, self.back_button_color, self.back_button_rect, border_radius=20)
            back_text_rect = self.back_button_text_surface.get_rect(center=self.back_button_rect.center)
            self.screen.blit(self.back_button_text_surface, back_text_rect)


            pygame.display.flip()

        pygame.quit()
        sys.exit()