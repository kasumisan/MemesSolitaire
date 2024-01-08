import pygame
import random
import time
import os


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
        self.background = pygame.image.load(os.path.join('data', 'game_data', 'fon.jpg'))
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))

        # Загрузка изображений карточек
        self.cards_path = 'data/cards'
        self.card_images = [pygame.image.load(os.path.join(self.cards_path, f)) for f in os.listdir(self.cards_path)]

        self.card_images_count = {img: 0 for img in self.card_images}

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
        self.font = pygame.font.SysFont('Impact', 30)
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
            elapsed_time = int(time.time() - self.start_time)
            timer_display = self.font.render(f'Время: {elapsed_time}', True, (255, 255, 255))
            self.screen.blit(timer_display, (self.WIDTH - 150, 10))
            pygame.mouse.set_visible(False)
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.screen.blit(self.cursor_img, (x, y))

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
