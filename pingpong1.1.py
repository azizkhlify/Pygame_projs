

from time import sleep
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
import pygame
run=False
screen=pygame.display

def up():
    global run ,f,f2, screen
    f.close()
    
    f2.show()
    

app=QApplication([])
f2=loadUi('ppig2.ui')
f=loadUi('ppig.ui')
f.show()
f.po9.clicked.connect(up)
mus=True
def musi() :
    global mus
    if mus :
        mus=False 
        f2.music.setText('off')
    else :
        mus=True
        f2.music.setText('on')
dif2='normal'
def diff():
    global dif2
    if dif2=='normal':
        dif2='hard'
    elif dif2=='hard':
        dif2='easy'
    else : dif2='normal'
    f2.dif.setText(dif2)
ggs=5
def gg():
    global ggs , screen,run
    g=int(f2.goal.text())
    if g>0:
        ggs=g
    f2.close()
    screen=pygame.display.set_mode((800,600))
    run=True





f2.music.clicked.connect(musi)
f2.dif.clicked.connect(diff)
f2.sta.clicked.connect(gg)

app.exec_()






from random import randint
tab2=[]
tab1=[]
for x in range(40):
    tab1.append(randint(10,790))
for x in range(40):
    tab2.append(randint(10,590))
pygame.init()
font=pygame.font.Font('freesansbold.ttf',32)
pygame.display.set_caption('PingPong ')
gho=pygame.image.load('ghost.png')
imag=pygame.image.load('img.png')
bimag=pygame.image.load('circle.png')
po9=pygame.mixer.Sound('po9.wav')
wi=pygame.mixer.Sound('wi.wav')
tn=pygame.mixer.Sound('tntrn.wav')
prr=pygame.mixer.Sound('prr.wav')
if mus:prr.play(-1)
def scoreBord():
    sc=font.render('sisi 1 Score : '+ str(s1),True,(98, 255, 129))
    vi=font.render('sisi 2 Score : '+ str(s2),True,(98, 255, 129))
    screen.blit(sc,(10,10))
    screen.blit(vi,(510,10))
#col:(98, 255, 129,)(85, 0, 127)
def player1(x,y):
    screen.blit(imag,(x,y))
def player2(x,y):
    screen.blit(imag,(x,y))
def ball(x,y):
    screen.blit(bimag,(x,y))
def chang():
    global mvt 
    var=randint(0,3)
    if mvt=='s':
        if var==0:mvt='ul'
        if var==1:mvt='ur'
        if var==2:mvt='dl'
        if var==3:mvt='dr'
def win(i):
    global mvt ,bx,by,b,s1,s2
    mvt='s'
    s1,s2 = 0,0
    bx=350
    by=250
    text=font.render('Player '+ str(i) +' win !!',True,(98, 255, 129))
    screen.blit(text,(100,250))
    b=False
    tn.play()
    
def play():
    text=font.render('PRESS SPACE TO PLAY ',True,(98, 255, 129))
    screen.blit(text,(200,250))

#l3sa toulha : 180 !
b=True
bx=400
by=300
p1x=30
p1y=p1i=210
p2x=730
p2y=p2i=210
y1c=0
y2c=0
ch=1
s1=0
s2=0
mvt='s'
v=1
if dif2=='normal': ch=1
elif dif2=='hard' : ch=3
else: ch=0.5
bool=False

while run:
    p2y=by
    if mvt=='dl':
        bx-=ch
        by+=ch
    if mvt=='dr':
        bx+=ch
        by+=ch
    if mvt=='ul':
        bx-=ch
        by-=ch
    if mvt=='ur':
        bx+=ch
        by-=ch
    if p1y<=0:
        p1y =0
    if p1y>=600-179.5:
        p1y=600-179.5
    if p2y<=0:
        p2y =0
    if p2y>=600-179.5:
        p2y=600-179.5
    if by>=555:
        po9.play()
        if mvt=='dl':
            mvt='ul'
        if mvt== 'dr':
            mvt='ur'
    if by<=-5:
        po9.play()
        if mvt=='ur': mvt='dr'
        if mvt=='ul' : mvt = 'dl'
    if bx<=70:
        if p1y-50<=by<=p1y+180:
            po9.play()
            if mvt=='ul': mvt='ur'
            if mvt=='dl' : mvt = 'dr'
        else :
            wi.play()
            bx=71
            by=250
            i=randint(0,1)
            if i == 1 :
                mvt='ur'
            else : mvt ='dr'
            s2+=1
            ch+=0.005
            v+=0.005
    if 687<=bx:
        if p2y-50<=by<=p2y+180:
            po9.play()
            if mvt=='ur': mvt='ul'
            if mvt=='dr' : mvt = 'dl'
        else :
            wi.play()
            bx=686
            by=250
            i=randint(0,1)
            if i == 1 :
                mvt='ul'
            else : mvt ='dl'
            s1+=1
            ch+=0.005
            v+=0.005

    screen.fill((85, 0, 127))
    if bool :screen.blit(bit,(0,0))
    else:
        for i in range(40):
            screen.blit(gho,(tab1[i],tab2[i]))
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            run=False
        if event.type==pygame.KEYDOWN :
            if event.key==pygame.K_p:
                y2c-=v
            if event.key==pygame.K_l:
                y2c+=v
            if event.key==pygame.K_a:
                y1c-=v
            if event.key==pygame.K_s:
                y1c+=v
            if event.key==pygame.K_c :
                bimag=pygame.image.load('yass.png')
                bit=pygame.image.load('bitna.png')
                imag=pygame.image.load('sisi.png')
                po9=pygame.mixer.Sound('ynynyn.wav')
                wi=pygame.mixer.Sound('wi.wav')
                tn=pygame.mixer.Sound('wrrry.wav')
                prr=pygame.mixer.Sound('prr.wav')
                bool=True

            if event.key==pygame.K_SPACE :
                b=True 
                if mvt=='s':
                    chang()
                else : 
                    bx=350
                    by=250
                    mvt='s'
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_p or event.key==pygame.K_l:
                y2c=0
            if event.key==pygame.K_a or event.key==pygame.K_s:
                y1c=0
    
    p1y+=y1c
    p2y+=y2c
    player1(p1x,p1y)
    player2(p2x,p2y)
    if s1==ggs:
        win(1)
    if s2==ggs:
        win(2)
    if b :ball(bx,by)
    else :play()
    scoreBord()
    pygame.display.update()