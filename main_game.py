import pygame
from pygame.locals import *
import sys
import os
from os import path
from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, FPS, QUIT, BLACK, WHITE, RED, GREEN, B_GREEN, B_RED, YELLOW
from game_screen import load_assets
from game_screen import Arrow, Player, Background
import random
import numpy as np



pygame.display.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.mixer.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Run Run')
clock = pygame.time.Clock()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action(screen)         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont('freesansbold.ttf',20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
    

            
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

     
def quitgame(screen):
    pygame.quit()
    quit()
       
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(BLACK)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Run Run", largeText)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        #gameDisplay.blit(TextSurf, TextRect)
        
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!", 90,450,100,50, GREEN, B_GREEN, game_screen)
        button("QUIT", 291,450,100,50, RED, B_RED, quitgame)
        
        
                      
        #pygame.draw.rect(gameDisplay, RED,(291,450,100,50))

        pygame.display.update()
        clock.tick(15)
        
        
def crash(SCORE = 0):  
    
    HIGHSCORE = np.load("SCORE.npy")
    HIGHSCORE = np.append(HIGHSCORE, SCORE)
    
    if SCORE >= HIGHSCORE.max():
        np.save("SCORE.npy", np.append(HIGHSCORE, SCORE))
        
        
    
    gameDisplay.fill(BLACK)
    
    largeText = pygame.font.SysFont('freesansbold.ttf',90)
    smallText = pygame.font.SysFont('freesansbold.ttf',40)

    TextSurf, TextRect = text_objects("GAME OVER", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2 - 150))
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("SCORE: " + str(SCORE), smallText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2 - 100))
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("HIGHSCORE: " + str(HIGHSCORE.max()), smallText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2 - 50))
    gameDisplay.blit(TextSurf, TextRect)
        
        

    while True:
        
        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again",90,450,100,50,GREEN,B_GREEN,game_screen)
        button("Quit",291,450,100,50,RED,B_RED,quitgame)

        pygame.display.update()
        clock.tick(15)         
        
        
        
        
#Fazer o background mexer
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
arrows_list = ["arrow_green_up_img","arrow_green_down_img","arrow_green_left_img","arrow_green_right_img","arrow_red_up_img","arrow_red_down_img","arrow_red_left_img","arrow_red_right_img"]



def game_screen(screen):

    
    assets = load_assets(img_dir, snd_dir, fnt_dir)
    


    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = assets["background"]
    back1 = Background(background, 0, 0)
    back2 = Background(background, 0, -HEIGHT)
    all_backs = pygame.sprite.Group()
    all_backs.add(back1)
    all_backs.add(back2)




    # Cria o personagem. O construtor será chamado automaticamente.
    player = Player(assets["player_img"])
    player_group = pygame.sprite.Group()
    player_group.add(player)

    directions = {"arrow_red_up_img":"down",  "arrow_red_down_img":"up", 'arrow_red_left_img':"right",
                  'arrow_red_right_img':"left", 'arrow_green_up_img':"up",'arrow_green_down_img':"down",
                  'arrow_green_left_img':"left",'arrow_green_right_img':"right"}

    PLAYING = 0
    ERROR = 1
    DONE = 2
    TIME = 0
    SCORE = 0

    state = PLAYING
    
    all_arrows = pygame.sprite.Group()

    while state != DONE and state != ERROR:
#    while True:
        TIME+=1
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botão, etc).
            
            # a cada segundo, cria uma arrow.
            if TIME % 100*FPS == 0:
                img = random.choice(list(directions.keys()))
                
                arrow = Arrow(assets[img])
                arrow.direction = directions[img]
                all_arrows.add(arrow)
                
            screen.fill(BLACK)
            
            # A cada loop, redesenha o fundo e os sprites

            all_backs.draw(screen)
           
            # screen.blit(background, background_rect)
            
            # Desenha as setas na tela.    
            all_arrows.draw(screen) 

            player_group.draw(screen)
            
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
            
            
                
            keys = pygame.key.get_pressed()  # verifica se alguma tecla foi clicada
            #Ajusta a velocidade do jogo.
            acertou = False
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
                                    acertou = True
                                else:
                                    state = ERROR
                                    crash(SCORE)
                                    return
                        
                            if event.key == pygame.K_a:
                                if direct == "left":
                                    all_arrows.remove(arrow)
                                    acertou = True                                
                                else:
                                    state = ERROR
                                    crash(SCORE)
                                    return
                        
                            if event.key == pygame.K_w:
                                if direct == "up":
                                    all_arrows.remove(arrow)
                                    acertou = True                                
                                else:
                                    state = ERROR
                                    crash(SCORE)
                                    return
                        
                            if event.key == pygame.K_s:
                                if direct == "down":
                                    all_arrows.remove(arrow)
                                    acertou = True                                
                                else:
                                    state = ERROR
                                    crash(SCORE)
                                    return
                                
                        for back in all_backs:
                            if acertou:
                                back.move()
                                SCORE += 100
                            if back.rect.top > HEIGHT:
                                back.reset()

                        
    
#        # Desenha o score
#        smallText = pygame.font.SysFont('freesansbold.ttf',40)
#
#        text_surface = smallText.render("{:08d}".format(SCORE), True, YELLOW)
#        text_rect = text_surface.get_rect()
#        text_rect.center = (WIDTH / 2,  HEIGHT/2)
#        screen.blit(text_surface, text_rect)
#    

#        text_surface = score_font.render(chr(9829) * lives, True, RED)
#        text_rect = text_surface.get_rect()
#        text_rect.bottomleft = (10, HEIGHT - 10)
#        screen.blit(text_surface, text_rect)
#    
#    return QUIT
        
                                
game_intro()

game_screen(screen)


