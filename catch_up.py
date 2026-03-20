from pygame import *
from random import randint
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("пинпонг")
background = transform.scale(image.load('background.png'), (win_width, win_height))

game = True
clock = time.Clock()
speed = 10
finish = False
speed_x = 3
speed_y = 3

# mixer.init()
# mixer.music.load('')
# mixer.music.play()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        key_button = key.get_pressed()
        if key_button[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_button[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_R(self):
        key_button = key.get_pressed()
        if key_button[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_button[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

player_1 = Player('racket.png', 30, 200, 4, 50, 150)
player_2 = Player('racket.png', 620, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        player_1.reset()
        player_1.update_L()
        player_2.reset()
        player_2.update_R()
        ball.reset()
        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1 
    display.update()
    clock.tick(60) 

