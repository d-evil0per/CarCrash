import pygame
import time,random,numpy as np
from datetime import datetime
import os.path
pygame.init()
dirname, filename = os.path.split(os.path.abspath(__file__))
os. chdir(dirname)
crash_sound = pygame.mixer.Sound("assets/crash.wav")
display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
grey=(178, 190, 195)
red=(192, 57, 43)
green=(16, 172, 132)
# blue=(0,0,255)
brown=(211, 84, 0)

gameIcon = pygame.image.load('assets/keys.png')

pygame.display.set_icon(gameIcon)
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

clock=pygame.time.Clock()

def check_score():
    if os.path.exists('data/score.npy')== False:
        score_card=[]
        score_card.append(0)
        # score_card.append('000')
        np.save(os.path.join("data","score"),score_card)
    score_data=np.load("data/score.npy")
    # print(score_data[0])
    font= pygame.font.SysFont(None,30)
    HighScore=font.render("HighScore: "+str(score_data[0]),True,black)
    # HighScore_date=font.render("HighScore_date: "+str(score_data[1]),True,black)
    gameDisplay.blit(HighScore,(display_width*0.8,0))
    # gameDisplay.blit(HighScore_date,(0,60))
    return int(score_data[0])




def savescore(point):
    score_card=[]
    now = datetime.now()
 
    print("now =", now)
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    score_card.append(point)
    # score_card.append(dt_string)
    np.save("data/score",score_card)


def score(count,speed):
    font= pygame.font.SysFont(None,30)
    text=font.render("Score: "+str(count),True,black)
    speed=font.render("Speed: "+str(speed)+ "km/h",True,black)
    gameDisplay.blit(text,(10,0))
    gameDisplay.blit(speed,(display_width*0.4,0))


def things(thingx,thingy,thingw,thingh,color,carImage):
    # pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
   
    gameDisplay.blit(carImage,(thingx,thingy))

def grass_left(glx,gly,glw,glh,color):
    pygame.draw.rect(gameDisplay,color,[glx,gly,glw,glh])
   
def grass_right(grx,gry,grw,grh,color):
    pygame.draw.rect(gameDisplay,color,[grx,gry,grw,grh])


def footpath_left(flx,fly,flw,flh,color):
    pygame.draw.rect(gameDisplay,color,[flx,fly,flw,flh])

def footpath_right(frx,fry,frw,frh,color):
    pygame.draw.rect(gameDisplay,color,[frx,fry,frw,frh])


def text_objects(msg,font): 
    textSurface=font.render(msg,True,white)
    return textSurface,textSurface.get_rect()


def message_display(msg):
    largeText=pygame.font.Font('freesansbold.ttf',80)
    TextSurf,TextRect=text_objects(msg,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    ####################################
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    message_display('You Crashed!!')

def car(carImage,x,y):
    gameDisplay.blit(carImage,(x,y))

def showkey(key):
    dk=pygame.image.load('assets/keys.png')
    gameDisplay.blit(dk,(display_width*0.1,display_height*0.8))
    font= pygame.font.SysFont(None,30)
    text=font.render(key,True,black)
    
    gameDisplay.blit(text,(display_width*0.1,display_height*0.92))
    # pygame.display.update()

def game_loop():
     ############
    pygame.mixer.music.load('assets/music.mp3')
    pygame.mixer.music.play(-1)
    ############
    gameExit = False
    x=(display_width*0.45)
    y=(display_height*0.80)
    carImage=pygame.image.load('assets/mycar.png')
    x_change=0
    y_change=0

    thing_startx = random.randrange(display_width*0.3,display_width*0.6)
    # print(thing_startx)
    # print(x)
    thing_starty = -600
    thing_speed=5
    thing_width=50
    thing_height=95
    
    glx=0
    glw=display_width*0.3
    gly=0
    glh=display_height

    flx=(display_width*0.3)
    flw=10
    fly=0
    flh=display_height

    frx=display_width*0.7
    frw=10
    fry=0
    frh=display_height

    grx=display_width*0.7
    grw=display_width
    gry=0
    grh=display_height

    

    car_width=50
    car_height=95
    carimg=pygame.image.load('assets/car_0.png')
    point=0
    
    showkeytext=''
    while not gameExit:

        for event in pygame.event.get():
            # carImage=pygame.image.load('mycar.png')
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    # carImage=pygame.image.load('mycar_l.png')
                    # car_width=95
                    # car_height=50
                    showkeytext='Going LEFT'
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    # carImage=pygame.image.load('mycar_r.png')
                    # car_width=95
                    # car_height=50
                    showkeytext='Going RIGHT'
                    x_change=5
                elif event.key==pygame.K_UP:
                    # carImage=pygame.image.load('mycar.png')
                    showkeytext='Going UP'
                    y_change=-5
                elif event.key==pygame.K_DOWN:
                    # carImage=pygame.image.load('mycar_d.png')
                    showkeytext='Going DOWN'
                    y_change=5
            else:
                showkeytext=''
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change=0
        x+=x_change
        y+=y_change
        gameDisplay.fill(grey)
        things(thing_startx,thing_starty,thing_width,thing_height,black,carimg)
        grass_left(glx,gly,glw,glh,green)
        grass_right(grx,gry,grw,grh,green)
        footpath_left(flx,fly,flw,flh,brown)
        footpath_right(frx,fry,frw,frh,brown)
       
        thing_starty+=thing_speed
    
        # thing_startx+=thing_speed



        car(carImage,x,y)
        hsp=check_score()
        score(point,thing_speed*10)
        showkey(showkeytext)
        if x>display_width-car_width or x<0:
            if hsp<point:
                    savescore(point)
            crash()
        if y>display_height-car_height or y<0:
            if hsp<point:
                    savescore(point)
            crash()
            
        if thing_starty>display_height:
            thing_starty=0-thing_height
            # thing_startx=random.randrange(0,display_width)
            thing_startx = random.randrange(display_width*0.3,display_width*0.6)
            point+=1
            if hsp<point:
                savescore(point)
                hsp=check_score()

            carno=random.randrange(0,5)
            carimg=pygame.image.load('assets/car_'+str(carno)+'.png')
            if thing_speed<20:
                thing_speed+=0.5
            
        if x<(display_width*0.3) or x>(display_width*0.65):
            crash()

        if y< thing_starty+thing_height:
            # print('y Crossover')
            if (x> thing_startx and x <thing_startx+thing_width  or x+car_width> thing_startx and x+car_width<thing_startx+thing_width) :
                # print('Xcrossover')
                if hsp<point:
                    savescore(point)
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()

