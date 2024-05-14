import pygame
import random
from jogador import *
from obstaculos import *
from objetivos import *
import time
pygame.init()
# Definir as cores
pontuacao = 0
vidas = 5
tela = pygame.display.set_mode((800,500)) #Escolhendo o tamanho da tela

pygame.display.set_caption("Fruit Drops") #Alterando o nome do jogo
clock = pygame.time.Clock() #Limitando o FPS
tela.fill((255,0,0)) #escolhendo a cor de fundo do jogo
#Configurando a fonte
fonte = pygame.font.SysFont(None,36)


rodando = True #fazendo o jogo rodar infinitamente
mario = Player('mario.png',50,50,350,500)
lista_inimigos = [Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),]

lista_objetivos = [Objetivos('cogumelo.png',25,30,0),
                   Objetivos('cogumelo.png',25,30,0),
                   Objetivos('cogumelo.png',25,30,0),
                   Objetivos('cogumelo.png',25,30,0),
                   Objetivos('cogumelo.png',25,30,0),
                   Objetivos('cogumelo.png',25,30,0),
                   Objetivos('cogumelo.png',25,30,0),
                   Objetivos('cogumelo.png',25,30,0),
                   Objetivos('cogumelo.png',25,30,0),
                   Objetivos('cogumelo.png',25,30,0)]

lista_bonus = [Objetivos('cogumelo_verde.png',25,30,0),
               Objetivos('cogumelo_verde.png',25,30,0),
               Objetivos('cogumelo_verde.png',25,30,0),]

while True:
    for evento in pygame.event.get():          
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((255,0,0))
    mario.movimento()
    mario.desenho(tela)
    for cogumelos_verde in lista_bonus:
        cogumelos_verde.movimento_obj()
        cogumelos_verde.desenho(tela)
        if mario.mascara.overlap(cogumelos_verde.mascara,(cogumelos_verde.pos_x-mario.pos_x , mario.pos_y-cogumelos_verde.pos_y)):
            cogumelos_verde.pos_x = random.randint(50,750)
            cogumelos_verde.velocidade = random.randint(1,10)
            pontuacao +=3
            cogumelos.pos_y=0
    for cogumelos in lista_objetivos:
        cogumelos.movimento_obj()
        cogumelos.desenho(tela)
        if mario.mascara.overlap(cogumelos.mascara,(cogumelos.pos_x-mario.pos_x , mario.pos_y-cogumelos.pos_y)):
            cogumelos.pos_x = random.randint(50,750)
            cogumelos.velocidade = random.randint(1,10)
            pontuacao +=1
            cogumelos.pos_y=0
    for inimigos in lista_inimigos:
        inimigos.movimento_inimigo2()
        inimigos.desenho(tela)
        if mario.mascara.overlap(inimigos.mascara,(inimigos.pos_x-mario.pos_x , mario.pos_y-inimigos.pos_y)):
            inimigos.pos_x = random.randint(50,750)
            inimigos.velocidade = random.randint(1,10)
            pontuacao -= 1
            mario.pos_x = 350
            mario.pos_y = 500
            inimigos.pos_y = 0

    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}",True,(0,255,0))
    tela.blit(texto_pontuacao,(0,10))
   
    
    pygame.display.update()
    clock.tick(60)
    
