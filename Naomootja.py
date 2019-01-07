import pygame
import random

from pygame.locals import *
        
class taust(pygame.sprite.Sprite):
    def __init__(self, pilt):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pilt)
        self.rect = self.image.get_rect()

def main():
    
    pygame.init()
    ekraaniLaius = 400
    ekraaniKõrgus = 525

    
    ekraan = pygame.display.set_mode([ekraaniLaius, ekraaniKõrgus])
    
    taustaPilt = taust("")           ##Sisestab pildi
    
    ekraan.blit(taustaPilt.image, taustaPilt.rect)
    
    done = False
    
    lõpetab = False
    
    andmed_list_x = []
    andmed_list_y = []
    
    mouse_x = 0
    mouse_y = 0

    while not done:
        
        loendur = 0
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                done = True 
     
            elif event.type == pygame.MOUSEBUTTONDOWN:    ##([Left Point - Right Point] : 2) + Right Point
                loendur += 1
                mouse = pygame.mouse.get_pos()
                
                mouse_x = mouse[0]
                mouse_y = mouse[1]
            
                andmed_list_x.append(mouse_x)
                andmed_list_y.append(mouse_y)
                
                ekraan.fill([255, 255, 255])
                ekraan.blit(taustaPilt.image, taustaPilt.rect)
                pygame.draw.line(ekraan, (255,   0,   0), [0, mouse_y], [800,mouse_y], 1)
                pygame.draw.line(ekraan, (255,   0,   0), [mouse_x, 0], [mouse_x,600], 1)
                
                for i in range(len(andmed_list_x)):
                    pygame.draw.circle(ekraan, (  0,   0, 255), [andmed_list_x[i], andmed_list_y[i]], 2)  
                
                if(loendur >= 1):
                    mouse_x = 0
                    mouse_y = 0
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    print(andmed_list_x.pop(len(andmed_list_x) - 1))
                    print(andmed_list_y.pop(len(andmed_list_y) - 1))
                    for i in range(len(andmed_list_x)):
                        pygame.draw.circle(ekraan, (  0,   0, 255), [andmed_list_x[i], andmed_list_y[i]], 2)  
                
        
        pygame.display.flip()
    
    pygame.quit()
    
main()