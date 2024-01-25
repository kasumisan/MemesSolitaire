import pygame
import os
import sqlite3
from datetime import datetime

SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 700

bg = pygame.image.load('data/game_data/bg.jpg')


class Player(pygame.sprite.Sprite):
    right = True

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/game_data/idle.png')
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.score = 0

    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 10
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -16

    def go_left(self):
        self.change_x = -9
        if self.right:
            self.flip()
        self.right = False

    def go_right(self):
        self.change_x = 9
        if not self.right:
            self.flip()
        self.right = True

    def stop(self):
        self.change_x = 0

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load('data/game_data/platform.png')
        self.rect = self.image.get_rect()


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('data/game_data/coin.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Level(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.player = player
        self.score = 0

    def update(self):
        self.platform_list.update()
        self.coin_list.update()
        player_hit_list = pygame.sprite.spritecollide(self.player, self.coin_list, True)
        for coin in player_hit_list:
            self.score += 10

    def draw(self, screen):
        screen.blit(bg, (0, 0))
        self.platform_list.draw(screen)
        self.coin_list.draw(screen)
        for coin in self.coin_list:
            if coin.alive():
                screen.blit(coin.image, coin.rect)

        font = pygame.font.Font('data/MP Manga.ttf', 36)
        score_text = font.render("Очки: " + str(self.score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))


class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        level = [
            [210, 32, 500, 500],
            [210, 32, 200, 400],
            [210, 32, 600, 300],
            [210, 32, 400, 200],
            [210, 32, 100, 100],
            [210, 32, 100, 800],
            [210, 32, 450, 700],
            [210, 32, 700, 600]
        ]
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        coins = [
            [400, 500],
            [200, 500],
            [600, 500],
        ]
        for coin in coins:
            coin_obj = Coin(coin[0], coin[1])
            self.coin_list.add(coin_obj)


class Play:
    def run(self):
        start_time = pygame.time.get_ticks()
        cursor_img = pygame.image.load(os.path.join('data', 'arrow.png'))
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Платформер")
        player = Player()
        level_list = []
        level_list.append(Level_01(player))
        current_level_no = 0
        current_level = level_list[current_level_no]
        active_sprite_list = pygame.sprite.Group()
        player.level = current_level
        player.rect.x = 340
        player.rect.y = SCREEN_HEIGHT - player.rect.height
        active_sprite_list.add(player)
        done = False
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_UP:
                        player.jump()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()
            if len(current_level.coin_list) == 0:
                end_time = pygame.time.get_ticks()

                play_time = (end_time - start_time) / 1000
                result_window = ResultWindow(current_level.player.score, play_time)
                result_window.display()
                done = True

            active_sprite_list.update()
            current_level.update()
            if player.rect.right >= SCREEN_WIDTH:
                player.rect.right = SCREEN_WIDTH

            if player.rect.left <= 0:
                player.rect.left = 0
            current_level.draw(screen)
            active_sprite_list.draw(screen)

            clock.tick(60)
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                screen.blit(cursor_img, (x, y))
            pygame.mouse.set_visible(False)
            pygame.display.flip()

        pygame.quit()


class ResultWindow:
    def __init__(self, score, play_time):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.score = score
        self.play_time = play_time

    def display(self):
        pygame.init()
        size = [800, 450]
        screen = pygame.display.set_mode(size)
        background = pygame.image.load(os.path.join('data', 'game_data', 'fon4.jpg'))
        screen.blit(background, (0, 0))
        pygame.display.set_caption("Результаты")

        font = pygame.font.Font('data/MP Manga.ttf', 36)
        title_text = font.render("Вы собрали все монеты!", True, (255, 255, 255))
        time_text = font.render("Время: " + str(round(self.play_time, 2)) + " сек", True, (255, 255, 255))
        screen.blit(title_text, (160, 150))
        screen.blit(time_text, (250, 300))

        pygame.display.flip()

        # Save data to SQLite database
        conn = sqlite3.connect('game_data.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS results (score INTEGER, play_time REAL, date TEXT)")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO results (score, play_time, date) VALUES (?, ?, ?)", (self.score, self.play_time, date))
        conn.commit()
        conn.close()

        pygame.time.wait(3000)  # Wait for 3 seconds before closing the window
        from main import GameLauncher
        gamelau = GameLauncher()
        gamelau.run()
