import pygame
import random
import time
import os
import sys
import sqlite3
from animation import MySprite


class MemoryGame:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()

        # Установка параметров окна
        self.size = self.WIDTH, self.HEIGHT = 800, 450
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("solitaire≽^•⩊•^≼")
        self.cursor_img = pygame.image.load(os.path.join('data', 'arrow.png'))
        # Загрузка изображения фона
        self.background = pygame.image.load(os.path.join('data', 'game_data', 'fon4.jpg'))
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))

        # Загрузка изображений карточек
        self.cards_path = 'data/cards'
        self.card_images = [pygame.image.load(os.path.join(self.cards_path, f)) for f in os.listdir(self.cards_path)]

        self.card_images_count = {img: 0 for img in self.card_images}
        self.my_sprite = MySprite()
        self.my_group = pygame.sprite.Group(self.my_sprite)
        clock = pygame.time.Clock()

        # Создание списка карточек
        self.cards = []
        for _ in range(6):
            for img in self.card_images:
                if self.card_images_count[img] < 2:
                    self.cards.append(img)
                    self.card_images_count[img] += 1

        # Перемешивание списка карточек
        random.shuffle(self.cards)

        # Отображение фона
        self.screen.blit(self.background, (0, 0))

        # Отображение окна
        pygame.display.flip()

        # Обратная сторона карточки
        self.card_back = pygame.image.load(os.path.join('data', 'game_data', 'back.jpg'))
        self.card_back = pygame.transform.scale(self.card_back, (100, 140))

        # Переменные для угаданных карточек
        self.first_card = None
        self.matched = []

        # Отображение баллов в верхнем левом углу
        self.font = pygame.font.Font('data/MP Manga.ttf', 30)
        self.score = 0

        # Отображение таймера в верхнем правом углу
        self.start_time = time.time()

    def run_game(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, rect in enumerate(self.card_rects):
                        if rect.collidepoint(mouse_pos) and i not in self.matched:
                            if self.first_card is None:
                                self.first_card = i
                            else:
                                if self.cards[self.first_card] == self.cards[i]:
                                    self.matched.extend([self.first_card, i])
                                    self.score += 10
                                self.first_card = None

            # Отображение фона
            self.screen.blit(self.background, (0, 0))

            # Отображение карточек
            for i, rect in enumerate(self.card_rects):
                if i in self.matched:
                    continue
                if i == self.first_card:
                    self.screen.blit(self.cards[i], (rect.x, rect.y))
                else:
                    self.screen.blit(self.card_back, (rect.x, rect.y))

            # Отображение счёта
            score_display = self.font.render(f'Очки: {self.score}', True, (255, 255, 255))
            self.screen.blit(score_display, (10, 10))

            # Отображение таймера
            self.elapsed_time = int(time.time() - self.start_time)
            timer_display = self.font.render(f'Время: {self.elapsed_time}', True, (255, 255, 255))
            self.screen.blit(timer_display, (self.WIDTH - 160, 10))
            pygame.mouse.set_visible(False)
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.screen.blit(self.cursor_img, (x, y))
            if self.score >= 60:
                self.show_result_window()
                self.stop_timer()
                # Обновление окна
            pygame.display.flip()

        pygame.quit()

    def stop_timer(self):
        self.elapsed_time = int(time.time() - self.start_time)  # Store elapsed time

    def show_result_window(self):
        result_displayed = False
        while not result_displayed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.my_group.update()
            self.background = pygame.image.load(os.path.join('data', 'game_data', 'fon4.jpg'))
            self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
            self.screen.blit(self.background, (0, 0))
            result_text = "Поздравляем, вот ваш результат:"
            result_font = pygame.font.Font('data/MP Manga.ttf', 36)
            result_surf = result_font.render(result_text, True, (255, 255, 255))
            result_rect = result_surf.get_rect(center=(400, 100))
            self.screen.blit(result_surf, result_rect)

            score_text = f'Очки: {self.score}'
            score_surf = self.font.render(score_text, True, (255, 255, 255))
            score_rect = score_surf.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2 - 50))
            self.screen.blit(score_surf, score_rect)

            time_text = f'Время: {self.elapsed_time} сек'
            time_surf = self.font.render(time_text, True, (255, 255, 255))
            time_rect = time_surf.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2 - 85))
            self.screen.blit(time_surf, time_rect)
            home_button = pygame.Rect(50, 350, 700, 50)
            pygame.draw.rect(self.screen, (255, 255, 255), home_button, border_radius=10)
            home_surf = pygame.Surface((700, 50), pygame.SRCALPHA)
            pygame.draw.rect(home_surf, (255, 20, 147, 200), (0, 0, 700, 50), border_radius=10)
            home_font = pygame.font.Font('data/MP Manga.ttf', 20)
            home_text = home_font.render('Нажмите в любом месте, чтобы вернуться домой', True, (255, 255, 255))
            home_rect = home_text.get_rect(center=home_surf.get_rect().center)
            home_surf.blit(home_text, home_rect)
            self.screen.blit(home_surf, home_button)
            self.my_group.draw(self.screen)
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.screen.blit(self.cursor_img, (x, y))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.save_to_database()
                    result_displayed = True
                    from main import GameLauncher
                    gamelau = GameLauncher()
                    gamelau.run()

                    break
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(20)

    def save_to_database(self):
        conn = sqlite3.connect('game_results.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS game_results (score INTEGER, time_taken INTEGER)')
        c.execute('INSERT INTO game_results (score, time_taken) VALUES (?, ?)', (self.score, self.elapsed_time))
        conn.commit()
        conn.close()

    def start_game(self):
        # Отображение карточек
        card_width = 100
        card_height = 140
        x = 50
        y = 50
        self.card_rects = []
        for card in self.cards:
            card = pygame.transform.scale(card, (card_width, card_height))
            self.screen.blit(card, (x, y))
            self.card_rects.append(pygame.Rect(x, y, card_width, card_height))
            x += card_width + 20
            if x > self.WIDTH - card_width:
                x = 50
                y += card_height + 20

        # Отображение окна
        pygame.display.flip()
        pygame.time.wait(3000)

        # Запуск игры
        self.run_game()


kamina_game = MemoryGame()
kamina_game.start_game()
