import pygame 
from player import player
pygame.init()
screen=pygame.display.set_mode((800,600))
lev1=pygame.image.load('lev1.png')
s=pygame.image.load('sisi.png')
class orsa(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.vit=8
        self.image=pygame.image.load('sisi.png')
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=300
sisi=orsa()



l=1
ynyn=player()
r=True 
j=16
while r:
    if ynyn.pressed.get(pygame.K_d) and ynyn.can_move:
            ynyn.go_right()
    if ynyn.pressed.get(pygame.K_q) and ynyn.can_move:
            ynyn.go_left()
    sisi.rect.y+=sisi.vit
    if sisi.rect.y>400 or sisi.rect.y<0:
        sisi.vit=-sisi.vit

    if l==1:
        lev=lev1
    screen.fill((0,0,0))
    screen.blit(lev,(0,0))
    if ynyn.jump:
        ynyn.jump-=1
        ynyn.rect.y-=j
        if j%10==0:
            j-=1
    elif not ynyn.in_sol : 
        ynyn.rect.y+=15
        j=16
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            r=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                ynyn.jumping()
            else :ynyn.pressed[event.key]=True 



                
        if event.type==pygame.KEYUP:
            ynyn.pressed[event.key]=False 
    if l==1:
        #sols
        if 160>=ynyn.rect.y>=140 and ynyn.rect.x<=200:ynyn.rect.y , ynyn.in_sol , ynyn.can_move=145 , True , True 
        elif 260<=ynyn.rect.y<=280 and ynyn.rect.x>=506:ynyn.rect.y , ynyn.in_sol , ynyn.can_move=260 , True ,True
        elif (350<=ynyn.rect.x<=450 ) and sisi.rect.y-120<=ynyn.rect.y<=sisi.rect.y-107:ynyn.rect.y , ynyn.in_sol , ynyn.can_move=sisi.rect.y-107 , True ,True

        else :
            ynyn.in_sol=False
        #obstacles
        if (300<=ynyn.rect.x<=450 ) and sisi.rect.y-100<=ynyn.rect.y<=sisi.rect.y+200:
            ynyn.can_move=False

        
    screen.blit(ynyn.image,ynyn.rect)   
    screen.blit(sisi.image,sisi.rect) 

    
    pygame.display.update()
