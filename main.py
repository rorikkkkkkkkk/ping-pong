from pygame import *

win_width = 600
win_height = 500
title = 'Ping-Pong!'
back = (198, 128, 0)

window = display.set_mode((win_width, win_height))
display.set_caption(title)
window.fill(back)

racket_width = 10
racket_height = 70

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < win_height - racket_height:
            self.rect.y += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < win_height - racket_height:
            self.rect.y += self.speed


game = True
finish = False
clock = time.Clock()
FPS = 25

font.init()
f1 = font.Font(None, 30)
l_lose = f1.render('Left Player Lose!!!', 1, (125, 0, 0))
r_lose = f1.render('Right Player Lose!!!', 1, (125, 0, 0))

speedx = 3
speedy = 3

l_player = Player('raketkapingpong.png', 30, 200, 5, racket_width, racket_height)
r_player = Player('raketkapingpong.png', 580, 200, 5, racket_width, racket_height)
ball = GameSprite('ballpp.png', 200, 200, 5, 50, 50)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)
        l_player.update_l()
        r_player.update_r()
        ball.rect.x += speedx
        ball.rect.y += speedy

        if sprite.collide_rect(l_player, ball) or sprite.collide_rect(r_player, ball):
            speedx *= -1

        if ball.rect.y < 0 or ball.rect.y > 450:
            speedy *= -1

        if ball.rect.x > 550:
            finish = True
            window.blit(r_lose, (200, 200))

        if ball.rect.x < 0:
            finish = True
            window.blit(l_lose, (200, 200))

        r_player.reset()
        l_player.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)






