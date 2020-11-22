from time import *
import pygame
from pygame import mixer

import game_config as gc
import game_config2 as gc2
import game_config3 as gc3

from pygame import display, event, image
from animal import Animal
from animal2 import Animal2
from animal3 import Animal3
import sys

pygame.init()

display.set_caption('Flip Out')

screen = display.set_mode((gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT))

font = pygame.font.Font('freesansbold.ttf', 40)
LargeText = pygame.font.Font('freesansbold.ttf',10)

BLACK = (0, 0, 0)
WHITE = (255,255,255)

RED = (200,0,0)
BRIGHT_RED = (255,0,0)

BRIGHT_GREEN = (0,255,0)
GREEN = (0,200,0)

YELLOW = (255,255,0)
BRIGHT_YELLOW = (255,255,153)

BRIGHT_ORANGE = (200,128,0)
ORANGE = (255,128,0)

BLUE = (0,0,255)
BRIGHT_BLUE = (0,0,200)


def textobj(text,font):
    textsurface = font.render(text,True,WHITE)
    return textsurface, textsurface.get_rect()

        
def message():
    largetext = pygame.font.Font('freesansbold.ttf',25)
    textsurf,textrect = textobj(text,largetext)
    textrect.center = (400,75)
    screen.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(2)
    gameloop()
    
def option(msg,x,y,w,h,inact,act,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,act,(x,y,w,h))

        if click[0] == 1 and action == "LEVEL 1":
            gameloop('L1',0)
        
        elif click[0] == 1 and action == "LEVEL 2":
            gameloop('L2',0)
            
        elif click[0] == 1 and action == "LEVEL 3":
            gameloop('L3',2)
            
        elif click[0] == 1 and action == "LEVEL 4":
            gameloop('L4',4)
        
        elif click[0] == 1 and action == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            pygame.draw.rect(screen,inact,(x,y,w,h))

        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = textobj(msg, smalltext)
        textRect.center = ((x+(w//2)),(y+(h//2)))
        screen.blit(textSurf,textRect)


def startmenu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = False
                    pygame.quit()
                    sys.exit()
                    
        screen.fill(BLACK)       
        LargeText = pygame.font.Font('freesansbold.ttf',75)
        TextSurf, TextRect = textobj("FLIP OUT",LargeText)
        TextRect.center = (400,75)
        screen.blit(TextSurf,TextRect)


        option("LEVEL 1",275,125,250,60,BLUE,BRIGHT_BLUE,"LEVEL 1")
        option("LEVEL 2",275,200,250,60,GREEN,BRIGHT_GREEN,"LEVEL 2")
        option("LEVEL 3",275,275,250,60,YELLOW,BRIGHT_YELLOW,"LEVEL 3")
        option("LEVEL 4",275,350,250,60,ORANGE,BRIGHT_ORANGE,"LEVEL 4")
        option("QUIT",275,425,250,60,RED,BRIGHT_RED,"QUIT")
        
        mouse = pygame.mouse.get_pos()
        if 275+250 > mouse[0] > 275 and 125+60 > mouse[1] > 125:
            pygame.draw.rect(screen,BRIGHT_BLUE,(275,125,250,60))
        else:
            pygame.draw.rect(screen,BLUE,(275,125,250,60))

        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = textobj("LEVEL 1", smalltext)
        textRect.center = ((275+(250//2)),(125+(60//2)))
        screen.blit(textSurf,textRect)


        if 275+250 > mouse[0] > 275 and 200+60 > mouse[1] > 200:
            pygame.draw.rect(screen,BRIGHT_GREEN,(275,200,250,60))
        else:
            pygame.draw.rect(screen,GREEN,(275,200,250,60))
            
        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = textobj("LEVEL 2", smalltext)
        textRect.center = ((275+(250//2)),(200+(60//2)))
        screen.blit(textSurf,textRect)


        if 275+250 > mouse[0] > 275 and 275+60 > mouse[1] > 275:
            pygame.draw.rect(screen,BRIGHT_YELLOW,(275,275,250,60))
        else:
            pygame.draw.rect(screen,YELLOW,(275,275,250,60))
            
        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = textobj("LEVEL 3", smalltext)
        textRect.center = ((275+(250//2)),(275+(60//2)))
        screen.blit(textSurf,textRect)


        if 275+250 > mouse[0] > 275 and 350+60 > mouse[1] > 350:
            pygame.draw.rect(screen,BRIGHT_ORANGE,(275,350,250,60))
        else:
            pygame.draw.rect(screen,ORANGE,(275,350,250,60))
            
        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = textobj("LEVEL 4", smalltext)
        textRect.center = ((275+(250//2)),(350+(60//2)))
        screen.blit(textSurf,textRect)


        if 275+250 > mouse[0] > 275 and 425+60 > mouse[1] > 425:
            pygame.draw.rect(screen,BRIGHT_RED,(275,425,250,60))
        else:
            pygame.draw.rect(screen,RED,(275,425,250,60))
            
        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = textobj("QUIT", smalltext)
        textRect.center = ((275+(250//2)),(425+(60//2)))
        screen.blit(textSurf,textRect)
            
        pygame.display.update()

def gameloop(level,dmatch):
    
    def find_index_from_xy(x, y):
        row = y // gc.IMAGE_SIZE
        col = x // gc.IMAGE_SIZE
        index = row * gc.NUM_TILES_SIDE + col
        return row, col, index

    def draw_timer(screen, x, y, time_left):
        if level == 'L1':
            font = pygame.font.Font(None, 40)
            text = font.render("No time limit.",True,BLACK,WHITE)
            screen.blit(text, (x, y))
        else:
            if (game_time - time_left) <= 10:
                pygame.draw.rect(screen,WHITE,(x,y,250,60))
                font = pygame.font.Font(None, 40)
                text = font.render("Time Left = " + str(game_time - time_left),True,RED,WHITE)
                screen.blit(text,(x, y))
                display.flip()
                
            else:
                font = pygame.font.Font(None, 40)
                text = font.render("Time Left = " + str(game_time - time_left),True,BLACK,WHITE)
                screen.blit(text,(x, y))
                display.flip()
                

    def match_chances(screen, x, y, chances_left):
        if level == 'L1':
            font = pygame.font.Font(None, 40)
            text = font.render("No chance limit.",True,BLACK,WHITE)
            screen.blit(text,(x, y))
            display.flip()
        else:
            if chances_left <= 5:
                font = pygame.font.Font(None, 40)
                text = font.render("Chances Left = " + str(chances_left),True,RED,WHITE)
                screen.blit(text,(x, y))
                display.flip()
            else:
                font = pygame.font.Font(None, 40)
                text = font.render("Chances Left = " + str(chances_left),True,BLACK,WHITE)
                screen.blit(text, (x, y))
                display.flip()

    
    buzzer = pygame.mixer.Sound('other_assets/Time-up.wav')
    match_sound = pygame.mixer.Sound('other_assets/Computer Error Alert.wav')
    success = pygame.mixer.Sound('other_assets/Success.wav')
    hiss = pygame.mixer.Sound('other_assets/Snake.wav')
    
    matched = image.load('other_assets/matched.png')
    win = image.load('other_assets/WINNER.png')
    timeout = image.load('other_assets/timeout.png')
    no_chance = image.load('other_assets/no chance.png')
    gameover = image.load('other_assets/gameover.png')

    if level == 'L1':
        tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
        game_time = 0
        chances_left = 0
    if level == 'L2':
        tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
        game_time = 30
        chances_left = 20

    elif level == 'L3':
        tiles = [Animal2(i) for i in range(0, gc.NUM_TILES_TOTAL)]
        game_time = 40
        chances_left = 15

    elif level == 'L4':
        tiles = [Animal3(i) for i in range(0, gc3.NUM_TILES_TOTAL)]
        game_time = 30
        chances_left = 12

    
    current_images_displayed = []
    unique = []
    
    
    mixer.music.load('other_assets/Level1_bgm.mp3')
    mixer.music.play(-1)
    
    start_time = int(pygame.time.get_ticks())


    running = True
    while running :
        time_left = pygame.time.get_ticks() - start_time 
        time_left = time_left / 1000
        time_left = int(time_left)
        draw_timer(screen, 510, 180, time_left)
        
        match_chances(screen,510,250,chances_left)

        if level != 'L1':
            if (start_time + (game_time * 1000) <= pygame.time.get_ticks()):
                mixer.music.pause()
                buzzer.play()
                sleep(0.5)
                screen.blit(timeout,(0,0))
                display.flip()
                sleep(2)
                running = False
                pygame.quit()
                sys.exit()
        
        current_events = event.get()

        for e in current_events:
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()


            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if(mouse_x <= 512 and mouse_y <= 512):
                    row, col, index = find_index_from_xy(mouse_x, mouse_y)
                    if index not in current_images_displayed:
                        if len(current_images_displayed) > 1:
                            current_images_displayed = current_images_displayed[1:] + [index]
                            confirm = all(item in unique for item in current_images_displayed)
                            if level != 'L1':
                                if not confirm:
                                    chances_left -= 1
                                if not chances_left:
                                    mixer.music.stop()
                                    buzzer.play()
                                    sleep(0.5)
                                    screen.blit(no_chance,(0,0))
                                    display.flip()
                                    sleep(2)
                                    running = False
                                    pygame.quit()
                                    sys.exit()
                                match_chances(screen, 550, 400, chances_left)
                        else:
                            current_images_displayed.append(index)
                
            screen.fill((255, 255, 255))
                

        total_skipped = 0
        for i, tile in enumerate(tiles):
            current_image = tile.image if i in current_images_displayed else tile.box
            if not tile.skip:
                screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
            else:
                total_skipped += 1

        display.flip()
        
        if len(current_images_displayed) == 2:
            index1 , index2 = current_images_displayed
            if tiles[index1].name == 'snake.png' and tiles[index2].name == 'snakes.png' or tiles[index1].name == 'snakes.png' and tiles[index2].name == 'snake.png' or tiles[index1].name == 'snakes.png' and tiles[index2].name == 'snakes.png' or tiles[index1].name == 'snake.png' and tiles[index2].name == 'snake.png':
                mixer.music.pause()
                hiss.play()
                sleep(0.5)
                screen.blit(gameover,(0,0))
                display.flip()
                sleep(2)
                running = False
                pygame.quit()
                sys.exit()
                
            if tiles[index1].name == tiles[index2].name:
                check = all(item in unique for item in current_images_displayed)
                if not check:
                    tiles[index1].skip = True
                    tiles[index2].skip = True
                    if total_skipped != len(tiles) - dmatch:
                        match_sound.play()
                        sleep(0.2)
                        screen.blit(matched,(0,0))
                        display.flip()
                        sleep(0.5)
                        unique.extend(current_images_displayed)
                        current_images_displayed = []

        if total_skipped == len(tiles) - dmatch:
            mixer.music.pause()
            success.play()
            screen.blit(win,(0,0))
            display.flip()
            sleep(2)
            running = False
            pygame.quit()
            sys.exit()

        
startmenu()
