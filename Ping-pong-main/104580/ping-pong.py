from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite) :
    def __init__ (self,player_image,player_x,player_y,size_x,size_y,player_speed,points) :
        super().__init__()
        self.size_x=size_x
        self.size_y=size_y
        self.image=transform.scale(image.load(player_image),(self.size_x,self.size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        self.points=points
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite) :
    def update_r(self) :
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>0 :
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y<400 :
            self.rect.y+=self.speed
    def update_l(self) :
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>0 :
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y<400 :
            self.rect.y+=self.speed
    #def fire(self) :
        #bullet=Bullet("bullet.png",self.rect.centerx,self.rect.top,10,20,2)
        #bullets.add(bullet)
        #kick.play()
        
Blue=(128,196,255)
win_width=700
win_lenght=500
window=display.set_mode((win_width,win_lenght))
game=True
finish=False
clock=time.Clock()
FPS=60
player=Player("ping_pong_r.png",0,200,60,100,3,0)
player2=Player("ping_pong_r.png",640,200,60,100,3,0)
ball=GameSprite("tennis_ball.png",300,250,75,45,4,0)
speed_x=3
speed_y=3
font.init()
font1=font.SysFont("Arial",40)
win1=font1.render("Player 1 win",True,(255,0,255))
win2=font1.render("Player 2 win",True,(255,0,255))
while game:
    for e in event.get() :
        if e.type==QUIT:
            game=False
    if finish!=True :
        window.fill(Blue)
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if ball.rect.y>win_lenght-30 or ball.rect.y<0 :
            speed_y*=-1
        if sprite.collide_rect(ball,player) :
            speed_x*=-1
        if sprite.collide_rect(ball,player2) :
            speed_x*=-1
        if ball.rect.x>700 :
            finish=True
           #window.blit(win1,(200,200))
           #player.points+=1
        if ball.rect.x<0 :
            finish=True
            #player2.points+=1
            #window.blit(win2,(200,200))
        player.reset()
        player.update_l()
        player2.reset()
        player2.update_r()
        ball.reset()
        ball.update()
    display.update()
    clock.tick(FPS)