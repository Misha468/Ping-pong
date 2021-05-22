from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x , player_y, weight, height , player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (weight ,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x , self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_s] and self.rect.y < 415:
            self.rect.y += self.speed  
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed  
speed_y = 3
speed_x = 3
ball = Player('ping_pong.png', 250, 250, 45,45, 5)
roketka1 = Player('roketka1.png', 5 ,250 ,85 , 90, 4)
roketka2 = Player('roketka2.png', 575, 250 , 45, 85, 4)
window = display.set_mode((700,500))
display.set_caption("PING_PONG")
fon = transform.scale(image.load("fon.jpg"), (700,500))
clock = time.Clock()
font.init()
font2 = font.SysFont('Arial' , 35)
lose1 = font2.render('ПЕРВЫЙ ИГРОК ПРОИГРАЛ!', True , (255 , 0 ,0))
lose2 = font2.render('ВТОРОЙ ИГРОК ПРОИГРАЛ!' , True , (255 , 0 , 0))
max_lost = 3
FPS = 300
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(fon , (0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(roketka1, ball) or sprite.collide_rect(roketka2 , ball):
        speed_x *= -1
    if ball.rect.x < -1:
        window.blit(lose1, (200 , 250))
    if ball.rect.x > 700:
        window.blit(lose2, (200,250))
    roketka1.reset()
    ball.reset()
    roketka2.reset()
    roketka1.update_l()
    roketka2.update_r()
    display.update()
    clock.tick(FPS)