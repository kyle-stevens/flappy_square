import pygame
from button import make_button
from pygame.locals import *
import time
from obstacle import Obstacle

pygame.init()
pygame.display.set_caption('flappy_square')

#DEFINE COLORS
black = (0, 0, 0)
white = (255, 255, 255)
volume = False #False plays music

win_X = 400
win_Y = 600

def menu():
    global volume
    music() #first call to get music started
    gamewindow = pygame.display.set_mode((win_X, win_Y))
    gamewindow.fill(white)

    #pygame.mixer.music.load('bensound-love.mp3')
    #pygame.mixer.music.play(-1)

    #BACKGROUND
    BACKGROUND = make_button('background.png', (0,0), gamewindow)

    #BUTTON CREATION
    START = make_button('start.png', (100, 50), gamewindow)
    SETTINGS = make_button('settings.png', (100, 175), gamewindow)
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #do nothing
                    time.sleep(500)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                print(mouse)
                if START[1].collidepoint(mouse):
                    print("start")
                    game()
                elif SETTINGS[1].collidepoint(mouse):
                    print("mute") #WILL BECOME MUTE/UNMUTE
                    music()
                    print(volume)
        pygame.display.update()


def game():

    obstacles = []

    obstacles.append(Obstacle())



    gamewindow = pygame.display.set_mode((win_X, win_Y))
    gamewindow.fill(white)

    #pygame.mixer.music.load('bensound-love.mp3')
    #pygame.mixer.music.play(-1)

    # BACKGROUND
    BACKGROUND = make_button('background.png', (0, 0), gamewindow)

    # BUTTON CREATION

    char_pos_x = 100
    char_pos_y = 300
    vel_y = 0
    gravity = 1
    round = 0
    running = True
    points = 0
    red = blue = green = 255.0
    while (running):

        if red > 0:
            red -= 0.25


        ground = Rect((0, 550), (400, 50))
        roof = Rect((0, 0), (400, 50))
        char = Rect((char_pos_x - 5, char_pos_y - 5), (10, 10))

        round += 1
        print(points)
        #print(round)
        if round%25 ==0:
            obstacles.append(Obstacle())


        gamewindow.fill((int(red), int(blue), int(green)))

        for o in obstacles:
            orect = o.update_pos(round)
            pygame.draw.rect(gamewindow, black, orect)
            if orect.colliderect(char):
                print("YOU DIED")
                game()
            #print(orect)
            if o.position_x < char_pos_x and not o.passed:
                points += 1
                o.passed = True
                pygame.mixer.music.load('PINGAS-Richard-89282878.mp3')
                #pygame.mixer.music.load('Hitting_Metal-Douglas_Vicente-1756278897.mp3')
                pygame.mixer.music.play(1)
            if o.position_x < -50:
                obstacles.remove(obstacles[0])

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # do nothing
                    time.sleep(500)
                elif event.key == pygame.K_SPACE:
                    if vel_y > 0:
                        vel_y = 0
                    vel_y -= 10
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                print(mouse)

        #print(char_pos_x, " ", char_pos_y)
        vel_y = (vel_y + gravity)
        char_pos_y = char_pos_y + vel_y

        if ground.colliderect(char) or roof.colliderect(char):
            print("YOU DIED")
            break
        elif char_pos_y <= 0:
            char_pos_y = 10
        pygame.draw.rect(gamewindow, black, roof)
        pygame.draw.rect(gamewindow, black, ground)
        pygame.draw.rect(gamewindow, black, char)
        pygame.display.update()
        delay = 50 - round*0.005
        if delay < 20:
            delay = 20
        print(delay)
        pygame.time.delay(int(delay))



def music():
    global volume
    if volume:
        pygame.mixer.music.fadeout(2500)
        print("stop")
        #pygame.mixer.music.stop()
        volume = False
    else:
        pygame.mixer.music.load('bensound-love.mp3')
        pygame.mixer.music.play(-1)
        volume = True

while True:
    game()