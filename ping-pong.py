from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < H - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < H - 80:
            self.rect.y += self.speed
        
back = (200, 255, 255)
W = 600
H = 500
window = display.set_mode((W, H))
window.fill(back)

game = True
finish = False
clock= time.Clock()
FPS = 60

racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tenis.ball.png", 200, 200, 4, 50, 50)


speed_x = 3
speed_y = 3
