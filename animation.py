import pygame


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('data/frames/frame1.png'))
        self.images.append(pygame.image.load('data/frames/frame2.png'))
        self.images.append(pygame.image.load('data/frames/frame3.png'))
        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(290, 200, 150, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
