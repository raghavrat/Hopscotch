import time
import random
import pygame
from pygame import *

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

timer = pygame.time.get_ticks()

screen_width = 1200
screen_height = 600

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

score = 0
additivenum = 5
additivecost = 10
multipliercost = 50
multipliernum = 1

pygame.mouse.set_visible(0)
screen = pygame.display.set_mode([screen_width, screen_height])

cookie = pygame.image.load(r'assets/cookie.png')
special_cookie = pygame.image.load(r'assets/special cookie.png')
special_cookie_max = pygame.image.load(r'assets/special cookie max.png')
square = pygame.image.load(r'assets/square.png')
special_square = pygame.image.load(r'assets/special square.png')
special_square_max = pygame.image.load(r'assets/special square max.png')
border = pygame.image.load(r'assets/border.png')
bg = pygame.image.load(r'assets/backround.png')
additive = pygame.image.load(r'assets/additive.png')
multiplier = pygame.image.load(r'assets/multiplier.png')
pause = pygame.image.load(r'assets/pause.png')
play = pygame.image.load(r'assets/play.png')
cursor = pygame.image.load(r'assets/cursor.png')
start_screen = pygame.image.load(r'assets/start_screen.png')
bg1 = pygame.image.load(r'assets/bg.png')
rectangle = square.get_rect()
seconds = 0
myTimer = 0
pauseRect = pause.get_rect()
playRect = play.get_rect()
Compass = pygame.font.Font("assets/CompassPro.ttf", 32)
counter = Compass.render('Score = ' + str(score), True, black)
counterRect = counter.get_rect()
timerText = Compass.render('Time left = ' + str(myTimer), True, black)
matchup = pygame.font.Font('assets/MatchupPro.ttf', 32)
multipliertimes = matchup.render('x' + str(multipliernum), True, black)
multipliertimesRect = multipliertimes.get_rect()
timeRect = timerText.get_rect()
timeRect.center = (600, 100)
multipliertimesRect.center = (1110, 350)
counterRect.center = (600, 200)

Shop = Compass.render('Shop', True, black)
shopRect = Shop.get_rect()
additiveText = Compass.render('Cost = ' + str(additivecost), True, black)
additiveTextRect = additiveText.get_rect()
additiveTextRect.center = (1110, 100)
shopRect.center = (1110, 50)

shopRect.center = (1110, 50)

running = True
multiplierText = Compass.render('Cost = ' + str(multipliercost), True, black)
multiplierTextRect = multiplierText.get_rect()
multiplierTextRect.center = (1110, 270)
BoxX = random.randint(0, 900)
BoxY = random.randint(0, 500)
additiveRect = additive.get_rect()
multiplierRect = multiplier.get_rect()
special_squareRect = special_square.get_rect()
special_cookieRect = special_cookie.get_rect()
additiveRect.center = (1110, 200)
multiplierRect.center = (1110, 350)

(special_squareX, special_squareY) = (special_squareRect.x, special_squareRect.y)
X1 = 0
X2 = -1200


class GameState():
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        global timer
        global start_screen
        global bg
        global X1
        global X2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running
                running = False
            elif event.type == pygame.KEYDOWN :
                self.state = 'main_game'
                timer = pygame.time.get_ticks()
        (x, y) = pygame.mouse.get_pos()

        if X1 == 1200:
            X1 = -1200
        elif X2 == 1200:
            X2 = -1200
        else:
            X1 += 1
            X2 += 1
        screen.fill((255, 255, 255))
        screen.blit(bg1, (X1, 0))
        screen.blit(bg1, (X2, 0))
        screen.blit(start_screen, (0, 0))
        screen.blit(cursor, (x, y))
        pygame.display.flip()

    def main_game(self):
        global BoxY
        global BoxX
        global score
        global multipliernum
        global additivecost
        global additivenum
        global multipliercost
        global additiveText
        global timerText
        global timeRect
        global timer
        global additiveTextRect
        global multiplierText
        global multiplierTextRect
        global multipliertimesRect
        global multipliertimes
        global counter
        global counterRect
        global pause
        global seconds
        global  seconds1

        global multiplierTextRect
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running

                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.mouse.get_pos() >= (BoxX, BoxY) and pygame.mouse.get_pos() <= (BoxX + 100, BoxY + 100):

                    score += 1 * multipliernum
                    print("a")
                    BoxX = random.randint(0, 900)
                    BoxY = random.randint(0, 500)
                    counter = Compass.render('Score = ' + str(score), True, black)
                    counterRect = counter.get_rect()
                    counterRect.center = (600, 200)
                    timer = pygame.time.get_ticks()
                elif additiveRect.collidepoint(pygame.mouse.get_pos()):
                    if score >= additivecost:
                        score -= additivecost
                        additivecost = int(additivecost * 1.2)

                        additivenum += 1
                        additiveText = Compass.render('Cost = ' + str(additivecost), True, black)
                        additiveTextRect = additiveText.get_rect()
                        additiveTextRect.center = (1110, 100)
                elif multiplierRect.collidepoint(pygame.mouse.get_pos()):
                    if score >= multipliercost:
                        score -= multipliercost
                        multipliercost = int(multipliercost * 1.2)

                        multipliernum += 1
                        multiplierText = Compass.render('Cost = ' + str(multipliercost), True, black)
                        multiplierTextRect = additiveText.get_rect()
                        multiplierTextRect.center = (1110, 270)
                        multipliertimes = matchup.render('x' + str(multipliernum), True, black)
                        multipliertimesRect = multipliertimes.get_rect()
                        multipliertimesRect.center = (1110, 350)
                elif pauseRect.collidepoint(pygame.mouse.get_pos()):
                    seconds1 = seconds
                    self.state = 'paused'

            screen.fill((255, 255, 255))
            (x, y) = pygame.mouse.get_pos()
            mousex = x - 37.5
            mousey = y - 37.5

            screen.blit(bg, (0, 0))

            screen.blit(additive, additiveRect)
            screen.blit(square, (BoxX, BoxY))
            screen.blit(timerText, timeRect)
            screen.blit(additiveText, additiveTextRect)
            screen.blit(multiplierText, multiplierTextRect)
            screen.blit(multiplier, multiplierRect)
            screen.blit(multipliertimes, multipliertimesRect)
            screen.blit(counter, counterRect)
            screen.blit(Shop, shopRect)
            screen.blit(pause, pauseRect)

            screen.blit(border, (1000, 0))

            #screen.blit(cookie, (mousex, mousey))
            screen.blit(cursor, (x, y))
            pygame.display.flip()
        seconds = int((pygame.time.get_ticks() - timer) / 1000)

        myTimer = additivenum - seconds
        timerText = Compass.render('Time left = ' + str(myTimer), True, black)
        timeRect = timerText.get_rect()
        timeRect.center = (600, 100)
        if seconds == 5:
            running = False
    def paused(self):
        global X1
        global X2
        global timer
        global seconds1
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if playRect.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'main_game'
                    timer = (pygame.time.get_ticks()/1000 - seconds1) * 1000
            elif event.type == pygame.QUIT:
                global  running
                running = False

        if X1 == 1200:
            X1 = -1200
        elif X2 == 1200:
            X2 = -1200
        else:
            X1 += 1
            X2 += 1
        screen.fill((255, 255, 255))
        screen.blit(bg1, (X1, 0))
        screen.blit(bg1, (X2, 0))
        screen.blit(play, playRect)
        screen.blit(cursor, pygame.mouse.get_pos())
        pygame.display.flip()

    def state_manager(self):
        global seconds1
        global seconds
        if self.state == 'intro':
            self.intro()
        elif self.state == 'main_game':
            self.main_game()
        elif self.state == 'paused':
            self.paused()
game_state = GameState()

while running:
    game_state.state_manager()

pygame.quit()
