import pygame
import os

#Iniciatizandu Pygame
pygame. Init()

#Definindo tamanho do janela pedrão
WIDTH, HEIGHT = 800, 600
screen = pygame.digiley.set_mode((WIDTH, HEIGHT), руgame.RESIZABLE) 
pygame.display.set_caption("mover Imagem com Setas")

#Definindo cor de fundo
BG_COLOR = (293, 0, 40) #cor de fundo Com tom escuro

#Carregar a imagen
image file "GAME\\player.png" # Coloque o nome correto da sua imagem aqui
if os.path.exists(image_file):
  img pygame.image.load(image_file).convert_alpha() = Carregar a imagem
  img recting.get_rect(center (WIDTH // 2, HEIGHT // 2)) Centraliza a imagen
else:
  print("Imagem não encontrada!")
  
#Velocidade de movimento
SPEED = 1 #pixels por movimento

#Função para centralizar a imagem conforme o tamanho da tela
def centralize_image():
  global img_rect, WIDTH, HEIGHT
  img_rect.center (WIDTH // 2, HEIGHT // 2) # Centraliza a imagem no centro da tela

#Variáveis para controle de redimensionamento
last width, last_height = WIDTH, HEIGHT

#Loop principal do jogo
running True
while running:
  for event in pygame.event.get():
    if event.type pygame.QUIT:
      running False

  # Verifica se o tamanho da janela foi alterado
  current_width, current_height = screen.get_size()
  
  #Se a janela foi redimensionada, centraliza a imagem
  if current_width != last_width or current_height 1/e = last_height:
    WIDTH, HEIGHT = current_width, current_height
    centralize_image() # Centraliza a imagem quando a janela mudar de tamanho
    last_width, last_height current_width, current_height

  # Pega as teclas pressionadas
  keys pygame.key.get_pressed()

  # Movimentação da imagem
  if keys [pygame.K_LEFT]:
  img rect.x - SPEED # Move para a esquerda
  if keys [pygame.K_RIGHT]:
  img_rect.x + SPEED # Move para a direita
  if keys [pygame.K_UP]:
  img_rect.y- SPEED # Move para cima
  if keys [pygame.K_DOWN]:
  img_rect.y + SPEED #Move para baixo

  # Preencher o fundo
  screen.fill(BG_COLOR)

  # Desenhar a imagem na tela
  screen.blit(img, img_rect.topleft)
  
  #Atualizar a tela
  pygame.display.flip()
