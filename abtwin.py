import pygame
import sys
import os


class AboutWindow:
    def __init__(self, screen):
        self.screen = screen
        self.GREEN = (0, 200, 0)
        self.font = pygame.font.Font('data/MP Manga.ttf', 25)
        self.version = "Версия игры: 0.1"
        self.developers = "Разработчики: "
        self.developers2 = "Швайкова Кира, "
        self.developers3 = "Симонова Арина"
        self.copyright = "2024, все права защищены"
        self.cursor_img = pygame.image.load(os.path.join('data', 'arrow.png'))
        self.back_button_color = (255, 255, 255)
        self.back_button_rect = pygame.Rect(50, self.screen.get_height() - 70, 150, 50)
        self.back_button_text = 'Назад'
        self.back_button_text_surface = self.font.render(self.back_button_text, True, (0, 0, 0))

    def show_window(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.back_button_rect.collidepoint(mouse_pos):
                        from main import GameLauncher
                        gamelau = GameLauncher()
                        gamelau.run()

            self.screen.fill(self.GREEN)
            background = pygame.image.load(os.path.join('data', 'game_data', 'fon.jpg'))
            self.screen.blit(background, (0, 0))
            text_y = 70
            version_text = self.font.render(self.version, True, (255, 20, 147))
            self.screen.blit(version_text, (50, text_y))

            text_y += 50
            developers_text = self.font.render(self.developers, True, (255, 20, 147))
            self.screen.blit(developers_text, (50, text_y))

            text_y += 50
            developers_text = self.font.render(self.developers2, True, (255, 20, 147))
            self.screen.blit(developers_text, (50, text_y))

            text_y += 50
            developers_text = self.font.render(self.developers3, True, (255, 20, 147))
            self.screen.blit(developers_text, (50, text_y))

            text_y += 50
            copyright_text = self.font.render(self.copyright, True, (255, 255, 255))
            self.screen.blit(copyright_text, (50, text_y))

            pygame.draw.rect(self.screen, self.back_button_color, self.back_button_rect, border_radius=20)
            back_text_rect = self.back_button_text_surface.get_rect(center=self.back_button_rect.center)
            self.screen.blit(self.back_button_text_surface, back_text_rect)
            pygame.mouse.set_visible(False)
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.screen.blit(self.cursor_img, (x, y))

            clock.tick(60)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
