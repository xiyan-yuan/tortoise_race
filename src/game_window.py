# -*- coding: UTF-8 -*-
import pygame
import random
import os
from src.user_window import *

class Game:

    def __init__(self, num):
        self.num = num
        self.run = False
        self.number_user = {}       
        for i in range(self.num):
            self.number_user["number %s: " % (i+1)] = ""
        
    def player_window(self):
        player = Player(self.num)
        self.number_user = player.number_user 
        player.start()

    def game_window(self):
        # Initialize the game engine
        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (50, 50)
    
        # Set the height and width of the self.screen
        SIZE = [800, 600]
         
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Tortoise Race")
         
        # Create position list
        self.position_list = []
        for i in range(self.num):
            x = 100
            y = i * 120
            self.position_list.append([x, y])  
            
        self.speed_list = [1, 3, 5, 7, 9]
        self.end_list = []

        self.start()            
         
        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()
        
    def start(self):
        BLUE = (72,118,255)
        RED = (255, 0, 0)
        WHITE = [255, 255, 255]  
        clock = pygame.time.Clock()
         
        # Loop until the user clicks the close button.
        done = False
        while not done:
         
            for event in pygame.event.get():   # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True   # Flag that we are done so we exit this loop
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # to: if game running               
                    x, y = event.pos                  
                    if (20 < x < 100) and (560 < y < 580):
                        self.player_window()                      
                    if (120 < x < 170) and (560 < y < 580):
                        for i in range(self.num):
                            self.position_list[i][0] = 100
                        self.run = True
                        self.end_list = []
         
            # Set the self.screen background
            self.screen.fill(WHITE)
            
            # Add RED line
            pygame.draw.line(self.screen,RED,(750,0),(750,540),1)   

            # Add player button
            carImg = pygame.image.load("add.jpg")
            small_img = pygame.transform.scale(carImg,(80, 20))
            self.screen.blit(small_img, (20, 560))
            carImg = pygame.image.load("start.jpg")
            small_img = pygame.transform.scale(carImg,(50, 20))
            self.screen.blit(small_img, (120, 560))
                    
            for i in range(self.num):
                random.shuffle(self.speed_list)
                            
                # Add tortoise
                text = pygame.font.Font("zk.ttf", 15)
                tortoise = text.render(self.number_user["number %s: " % (i+1)], 1, BLUE)
                self.screen.blit(tortoise, (20, self.position_list[i][1] + 20))
         
                # Draw the snow flake
                carImg = pygame.image.load("w.jpg")
                small_img = pygame.transform.scale(carImg,(50, 50))
                self.screen.blit(small_img, (self.position_list[i][0], self.position_list[i][1]))
         
                # Move the snow flake down one pixel
                if self.run:
                    self.position_list[i][0] += self.speed_list[i]
         
                # If the snow flake has moved off the bottom of the self.screen
                if self.position_list[i][0] >700:
                    self.position_list[i][0] = 700
                    if not i in self.end_list:
                        self.end_list.append(i)
                
            if len(self.end_list) == 5:
                i = 1
                for e in self.end_list:
                    text = pygame.font.Font("zk.ttf", 30)
                    current_user = text.render(str(i) + ": " + self.number_user["number %s: " % (e+1)], 1, BLUE)
                    self.screen.blit(current_user, (300, 80*i))
                    i += 1

                # Give it a new x position
                self.run = False
         
            # Go ahead and update the self.screen with what we've drawn.
            pygame.display.flip()
            clock.tick(20)