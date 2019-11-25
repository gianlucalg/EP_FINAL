import pygame
from pygame.locals import *
import sys
import os
from os import path
from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, FPS, QUIT, BLACK
from game_screen import load_assets
from game_screen import Arrow, Player, Background
import random


pygame.display.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.init()


#Fazer o background mexer
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        

arrows_list = ["arrow_green_up_img","arrow_green_down_img","arrow_green_left_img","arrow_green_right_img","arrow_red_up_img","arrow_red_down_img","arrow_red_left_img","arrow_red_right_img"]

all_backgrounds = pygame.sprite.Group()

#for i in range((HEIGHT+HEIGHT)/HEIGHT):
#    for j in range((WIDTH + WIDTH)/WIDTH):
#        all_backgrounds.add(Background(HEIGHT*i,WIDTH*j))


'''        
#Definir o display
    
#W, H = 576, 1024
#HW, HH = W / 2, H / 2
#AREA = W * H

#copiei essa linha de um vid n sei oq faz xD
#os.environ["n sei"] = "50,50"

#SET DO PYGAME
#personagem = pygame.image.load("img/a.png")
#pygame.init()
#CLOCK = pygame.time.Clock()
#DS = pygame.display.set_mode((W, H))
#pygame.display.set_caption("NOME DO JOGO")
#x = 0

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
    
'''

def game_screen(screen):
    
    all_backgrounds.update(pygame.cam)

    all_backgrounds.draw(screen)
    
    assets = load_assets(img_dir, snd_dir, fnt_dir)

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = assets["background"]
    background_rect = background.get_rect()

    # Cria o personagem. O construtor será chamado automaticamente.
    player = Player(assets["player_img"])

    directions = {"arrow_red_up_img":"down",  "arrow_red_down_img":"up", 'arrow_red_left_img':"right",
                  'arrow_red_right_img':"left", 'arrow_green_up_img':"up",'arrow_green_down_img':"down",
                  'arrow_green_left_img':"left",'arrow_green_right_img':"right"}

    PLAYING = 0
    ERROR = 1
    DONE = 2
    TIME = 0

    state = PLAYING
    
    all_arrows = pygame.sprite.Group()

    while state != DONE and state != ERROR:
        TIME+=1
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botão, etc).
            
            # a cada segundo, cria uma arrow.
            if TIME % 120*FPS == 0:
                                
                img = random.choice(list(directions.keys()))
                
                arrow = Arrow(assets[img])
                arrow.direction = directions[img]
                all_arrows.add(arrow)
            
            screen.fill(BLACK)
            
            # A cada loop, redesenha o fundo e os sprites
           
            screen.blit(background, background_rect)
            
            # Desenha as setas na tela.    
            all_arrows.draw(screen) 
            
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()       
                
            keys = pygame.key.get_pressed()  # verifica se alguma tecla foi clicada
            #Ajusta a velocidade do jogo.
            for event in pygame.event.get():
                    # print("OI")
                    
                    # Verifica se foi fechado.
                    if event.type == pygame.QUIT:
                        state = ERROR
                        return
                    
                    # Verifica se apertou alguma tecla.
                    if event.type == pygame.KEYDOWN:
                        for arrow in all_arrows:
                            direct = arrow.direction
                            if event.key == pygame.K_d:
                                if direct == "right":
                                    all_arrows.remove(arrow)
                                else:
                                    state = ERROR
                                    return
                        
                            if event.key == pygame.K_a:
                                if direct == "left":
                                    all_arrows.remove(arrow)
                                else:
                                    state = ERROR
                                    return
                        
                            if event.key == pygame.K_w:
                                if direct == "up":
                                    all_arrows.remove(arrow)
                                else:
                                    state = ERROR
                                    return
                        
                            if event.key == pygame.K_s:
                                if direct == "down":
                                    all_arrows.remove(arrow)
                                else:
                                    state = ERROR
                                    return
                    

game_screen(screen)