import pygame 

#Inicializando o Pygame
pygame.init()

#Definido o tamanho dajanela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set-caption("Janela simples")

#Loop principal do jogo
runnig = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    pygame.display.flip

#Finalizar o Pygame
pygame.quit()
