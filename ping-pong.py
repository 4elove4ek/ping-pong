from pygame import *
        
back = (200, 255, 255)
W = 600
H = 500
window = display.set_mode((W, H))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, file, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(file), (width, height))
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


game = True
finish = False
clock= time.Clock()
FPS = 60

racket1 = Player("racket.png", 30, 200, 4, 25, 150)
racket2 = Player("racket.png", 520, 200, 4, 25, 150)
ball = GameSprite("tenis_ball.png", W/2, H/2, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 5
speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball):
            speed_x *= -1
            ball.rect.x += 3

        if sprite.collide_rect(racket2, ball):
            speed_x *= -1
            ball.rect.x -= 3

        if ball.rect.y > H-30 or ball.rect.y < 0:
            speed_y *= -1
  
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
  
        if ball.rect.x > W:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()
 
    display.update()
    clock.tick(FPS)
