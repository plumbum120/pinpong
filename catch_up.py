from pygame import *
from random import randint
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("пинпонг")
background = transform.scale(image.load('background'), (win_width, win_height))

game = True
clock = time.Clock()
speed = 10
finish = False

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
    def update(self):
        key_button = key.get_pressed()
        if key_button[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_button[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.reset()
        player.update()

    display.update()
    clock.tick(60) 
