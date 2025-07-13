from pygame import *

window = display.set_mode((600,500))
bg = (153, 217, 234)
display.set_caption('Ping pong: multiplayer')

class Racket(sprite.Sprite):
    def __init__(self,keys,x):
        super().__init__()
        self.image = transform.scale(image.load('racket.png'),(50,150))
        self.keys = keys
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 175
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[self.keys[0]]:
            self.rect.y -= 5
        if keys_pressed[self.keys[1]]:
            self.rect.y += 5
        window.blit(self.image,(self.rect.x,self.rect.y))
class Ball(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = transform.scale(image.load('tenis_ball.png'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 225
    def update(self):
        global dx
        global dy
        self.rect.x += dx
        self.rect.y += dy
        if self.rect.y >= 450:
            dy *= -1
        if self.rect.y <= 0:
            dy *= -1
        window.blit(self.image,(self.rect.x,self.rect.y))

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOST! :(', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOST! :(', True, (180, 0, 0))
dx = 2
dy = 2
racket1 = Racket([K_w,K_s], 30)
racket2 = Racket([K_UP,K_DOWN], 520)
ball = Ball()
running = True
while running:
    window.fill(bg)
    racket1.update()
    racket2.update()
    ball.update()
    for e in event.get():
        if e.type == QUIT:
            running = False
    if ball.rect.colliderect(racket1.rect) or ball.rect.colliderect(racket2.rect):
        dx *= -1
    if ball.rect.x <= 0:
        window.blit(lose1, (200, 200))
        display.update()
        time.delay(5000)
        running = False
    elif ball.rect.x >= 550:
        window.blit(lose2, (200, 200))
        display.update()
        time.delay(5000)
        running = False
    display.update()
    time.Clock().tick(160)