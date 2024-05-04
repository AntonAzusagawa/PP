from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('gg2.png'), (700, 500))
clock = time.Clock()
FPS = 60
flowgame = True
pausegame = False
score1 = 0
score2 = 0

font.init()
font1 = font.SysFont('Arial', 70)
font2 = font.SysFont('Arial', 36)

lose1 = font1.render('lose of the first', True, (180, 0, 0))
lose2 = font1.render('lose of the first', True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 380:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 380:
            self.rect.y += self.speed

        

rocket1 = Player1('1337.png', 50, 250, 40, 120, 10)
rocket2 = Player2('1488.png', 600, 250, 40, 120, 10)
ball = GameSprite('232.png', 350, 250, 75, 75, 15)
speed_x = 3
speed_y = 3


while flowgame:
    for e in event.get():
        window.blit(background, (0, 0))
        if e.type == QUIT:
            flowgame = False
    if pausegame == False:
        window.blit(background, (0, 0))
        rocket1.update()
        rocket1.reset() 
        rocket2.update()
        rocket2.reset() 
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1.0005
            speed_y *= -1.0005

        if ball.rect.y > 425 or ball.rect.y < 0:
            speed_y *= -1.0005

        if ball.rect.x < 0:
            speed_x = 3
            speed_y = 3
            score2 += 1
            ball.rect.x = 350
            ball.rect.y = 250

        
        if ball.rect.x > 700:
            speed_x = 3
            speed_y = 3
            score1 += 1
            ball.rect.x = 350
            ball.rect.y = 250

        if score1 >= 10:
            pausegame = True       
            window.blit(lose2, (100, 200))
        
        if score2 >= 10:
            pausegame = True       
            window.blit(lose1, (100, 200))

        font3 = font.SysFont('Arial', 25) 
        scoreboard1 = font3.render(str(score1), True, (255, 255, 255))
        window.blit(scoreboard1, (325, 20))
        scoreboard2 = font3.render(str(score2), True, (255, 255, 255))
        window.blit(scoreboard2, (375, 20))

    
    display.update()
    clock.tick(FPS)
