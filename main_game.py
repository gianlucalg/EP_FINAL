import pygame
from pygame.locals import *
import sys
import os

#Fazer o background mexer
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
#Definir o display
    
W, H = 576, 1024
HW, HH = W / 2, H / 2
AREA = W * H

#copiei essa linha de um vid n sei oq faz xD
os.environ["n sei"] = "50,50"

#SET DO PYGAME
personagem = pygame.image.load("a.png")
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("NOME DO JOGO")
FPS = 120
bg = pygame.image.load("background.png").convert()
x = 0

#main loop
while True:
    events()
    
    rel_x = x % bg.get_rect().width
    DS.blit(bg, (0, rel_x - bg.get_rect().width))
    DS.blit(personagem, (0,100))
    if rel_x < W:
        DS.blit(bg, (0,rel_x))
    
    x += 2
    
    pygame.display.update()
    CLOCK.tick(FPS)