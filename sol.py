import pygame
import os
import random
import time

class MemoryGame:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()

        # Установка параметров окна
        self.win_width = 800
        self.win_height = 600
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption("Игра с карточками")

        # Загрузка изображения фона
        self.background = pygame.image.load(os.path.join('cards', 'fon.jpg'))
        self.background = pygame.transform.scale(self.background, (self.win_width, self.win_height))

        # Загрузка изображений карточек
        self.cards_path = 'data/cards'
        self.card_images = [pygame.image.load(os.path.join(self.cards_path, f)) for f in os.listdir(self.cards_path)]

        # Создание списка карточек
        self.cards = []
        for i in range(6):
            card = random.choice(self.card_images)
            self.cards.extend([card, card])

        # Перемешивание списка карточек
        random.shuffle(self.cards)

        # Отображение фона
        self.win.blit(self.background, (0, 0))

        # Отображение окна
        pygame.display.flip()
        pygame.time.wait(5000)

        # Обратная сторона карточки
        self.card_back = pygame.image.load(os.path.join('cards', 'back.jpg'))
        self.card_back = pygame.transform.scale(self.card_back, (100, 140))

        # Переменные для угаданных карточек
        self.first_card = None
        self.matched = []

        # Отображение баллов в верхнем левом углу
        self.font = pygame.font.SysFont(None, 36)
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
            self.win.blit(self.background, (0, 0))

            # Отображение карточек
            for i, rect in enumerate(self.card_rects):
                if i in self.matched:
                    continue
                if i == self.first_card:
                    self.win.blit(self.cards[i], (rect.x, rect.y))
                else:
                    self.win.blit(self.card_back, (rect.x, rect.y))

            # Отображение счёта
            score_display = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            self.win.blit(score_display, (10, 10))

            # Отображение таймера
            elapsed_time = int(time.time() - self.start_time)
            timer_display = self.font.render(f'Time: {elapsed_time}', True, (255, 255, 255))
            self.win.blit(timer_display, (self.win_width - 150, 10))

            # Обновление окна
            pygame.display.flip()

        pygame.quit()

    def start_game(self):
        # Отображение карточек
        card_width = 100
        card_height = 140
        x = 50
        y = 50
        self.card_rects = []
        for card in self.cards:
            card = pygame.transform.scale(card, (card_width, card_height))
            self.win.blit(card, (x, y))
            self.card_rects.append(pygame.Rect(x, y, card_width, card_height))
            x += card_width + 20
            if x > self.win_width - card_width:
                x = 50
                y += card_height + 20

        # Отображение окна
        pygame.display.flip()
        pygame.time.wait(3000)

        # Запуск игры
        self.run_game()

game = MemoryGame()
game.start_game()