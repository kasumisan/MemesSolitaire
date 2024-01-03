import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Определение размеров карты
CARD_WIDTH = 100
CARD_HEIGHT = 140
GAP = 20

# Загрузка изображений карт
card_images = []
for i in range(6):
    card_images.append(pygame.image.load(f"cards/card{i}.png"))

# Создание окна игры
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Найди пару")


# Класс Карта
class Card:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.is_face_up = False
        self.is_matched = False

    def draw(self, x, y):
        if self.is_face_up or self.is_matched:
            window_surface.blit(self.image, (x, y))
        else:
            pygame.draw.rect(window_surface, RED, (x, y, CARD_WIDTH, CARD_HEIGHT))


# Класс "Игра Найди пару"
class FindPairGame:
    def __init__(self):
        self.cards = []
        self.timer = 0
        self.score = 0
        self.previous_card = None

        self.setup_cards()

    def setup_cards(self):
        # Создание случайного списка с порядковыми номерами карт
        card_indices = list(range(6)) * 2
        random.shuffle(card_indices)

        # Создание карт и их позиционирование
        for i, index in enumerate(card_indices):
            row = i // 6
            col = i % 6
            x = 20 + col * (CARD_WIDTH + GAP)
            y = 200 + row * (CARD_HEIGHT + GAP)
            card = Card(card_images[index])
            card.rect.topleft = (x, y)
            self.cards.append(card)

    def draw(self):
        for card in self.cards:
            card.draw(card.rect.x, card.rect.y)

        # Отрисовка таймера
        font = pygame.font.Font(None, 40)
        timer_text = font.render(f"Time: {self.timer:.1f}", True, BLACK)
        timer_rect = timer_text.get_rect(topright=(WINDOW_WIDTH - 20, 20))
        window_surface.blit(timer_text, timer_rect)

        # Отрисовка количества очков
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        score_rect = score_text.get_rect(topleft=(20, 20))
        window_surface.blit(score_text, score_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            for card in self.cards:
                if card.rect.collidepoint(mouse_pos):
                    if not card.is_matched and not card.is_face_up:
                        card.is_face_up = True
                        if self.previous_card is None:
                            self.previous_card = card
                        else:
                            self.check_cards(card)
                            self.previous_card = None
                    break

    def check_cards(self, card):
        if card.image == self.previous_card.image:
            card.is_matched = True
            self.previous_card.is_matched = True
            self.score += 10
            if self.check_game_over():
                self.display_win_message()
        else:
            self.flip_cards_back(card, self.previous_card)

    def flip_cards_back(self, card1, card2):
        card1.is_face_up = False
        card2.is_face_up = False
        pygame.display.flip()
        time.sleep(1)

    def check_game_over(self):
        for card in self.cards:
            if not card.is_matched:
                return False
        return True

    def display_win_message(self):
        font = pygame.font.Font(None, 60)
        text_surface = font.render("Congratulations! You won!", True, BLACK)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window_surface.blit(text_surface, text_rect)

    def update_timer(self):
        if self.timer > 0:
            self.timer += 0.1
            time.sleep(0.1)  # Приостановка выполнения программы на 0.1 секунды

    def run(self):
        # Таймер отсчета времени
        time_left = 3
        for i in range(3, 0, -1):
            self.timer = time_left
            time.sleep(1)
            time_left -= 1

        start_time = time.time()
        running = True
        while running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.handle_event(event)

            # Очистка экрана
            window_surface.fill(WHITE)

            # Рисование игры
            self.draw()

            # Обновление таймера
            self.update_timer()

            # Обновление экрана
            pygame.display.flip()

            # Проверка на выигрыш
            if self.check_game_over():
                self.display_win_message()
                running = False

        # Завершение Pygame
        pygame.quit()


# Создание объекта игры "Найди пару"
game = FindPairGame()

# Запуск игры
game.run()
