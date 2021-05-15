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
        if keys_pressed[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_s] and self.rect.x < 595:
            self.rect.y += self.speed  
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y < 595:
            self.rect.y += self.speed  
roketka1 = Player('rocketka1.png', 5 ,420 ,65 , 65, 4)
window = display.set_mode((700,500))
display.set_caption("SHOTER")
fon = transform.scale(image.load("fon.jpg"), (700,500))
clock = time.Clock()
max_lost = 3
FPS = 300
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != False:
        window.blit(fon)
        roketka1.reset()
        roketka2.reset()
        roketka1.update_l()
        roketka2.update_r()
    display.update()
    clock.tick(FPS)