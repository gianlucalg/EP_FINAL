from os import path


img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
fnt_dir = path.join(path.dirname(__file__), 'font')


WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 120 # Frames por segundo


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 97)
GREEN = (0, 190, 90)
B_GREEN = (0, 255, 0)
B_RED = (255, 0, 0)
BLUE = (0, 200, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
