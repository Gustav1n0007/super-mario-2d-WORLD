import pygame
import random
from jogador import *
from obstaculos import *
from objetivos import *
import time
import os
pygame.init()
# Definir as cores
pontuacao = 0
vidas = 5
tela = pygame.display.set_mode((800,500)) #Escolhendo o tamanho da tela

pygame.display.set_caption("Fruit Drops") #Alterando o nome do jogo
clock = pygame.time.Clock() #Limitando o FPS
tela.fill((255,0,0)) #escolhendo a cor de fundo do jogo
#Configurando a fonte
fonte = pygame.font.SysFont('Berlin sans FB Demi',36)

# Definição do diretório onde está a música

# Carregamento da música
pygame.mixer.music.load('musica.mp3')
keys = pygame.key.get_pressed()
# Reprodução da música em loop (-1 para loop infinito)
pygame.mixer.music.play(-1)

rodando = True #fazendo o jogo rodar infinitamente
mario = Player('mario.png',50,50,350,500)
lista_inimigos = [Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
                  Obstaculos('casco.png',25,30,0),
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
fundo = Fundo('fundoMario.jpg',500,800,0,0)
marioWin = Fundo('marioWIn.png',400,170,100,100)
while True:
    for evento in pygame.event.get():          
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((255,0,0))
    fundo.desenho(tela)
    mario.movimento()
    mario.desenho(tela)
    for cogumelos_verde in lista_bonus:
        cogumelos_verde.movimento_obj()
        cogumelos_verde.desenho(tela)       
        if cogumelos_verde.pos_y > 500:
           cogumelos_verde.pos_x = random.randint(50,750)  
        if mario.mascara.overlap(cogumelos_verde.mascara,(cogumelos_verde.pos_x-mario.pos_x , mario.pos_y-cogumelos_verde.pos_y)):           
            cogumelos_verde.velocidade = random.randint(1,6)
            pontuacao +=3
            cogumelos.pos_y=0
    for cogumelos in lista_objetivos:
        cogumelos.movimento_obj()
        cogumelos.desenho(tela)
        
        if cogumelos.pos_y > 500:
           cogumelos.pos_x = random.randint(50,750)
        if mario.mascara.overlap(cogumelos.mascara,(cogumelos.pos_x-mario.pos_x , mario.pos_y-cogumelos.pos_y)):
            
            cogumelos.velocidade = random.randint(1,6)
            pontuacao +=1
            cogumelos.pos_y=0
    for inimigos in lista_inimigos:
        inimigos.movimento_inimigo2()
        inimigos.desenho(tela)
       
        if inimigos.pos_y > 500:
            inimigos.pos_x = random.randint(50,750)  
        if mario.mascara.overlap(inimigos.mascara,(inimigos.pos_x-mario.pos_x , mario.pos_y-inimigos.pos_y)):
            
            inimigos.velocidade = random.randint(1,6)
            vidas -=1
            mario.pos_x = 350
            mario.pos_y = 500
            inimigos.pos_y = 0
    
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}",True,(0,0,0))
    texto_vidas = fonte.render(f'Vidas: {vidas}',True,(0,0,0))
    tela.blit(texto_pontuacao,(0,10))
    tela.blit(texto_vidas,(0,40))
    texto_gameOver = fonte.render("Game Over", True,(0,0,0))
    texto_WIN = fonte.render("Você venceu", True,(0,0,0))
    if vidas == 0:
        fundo.desenho(tela)
        tela.blit(texto_gameOver,(320,200))
    if pontuacao == 100 or pontuacao >100:
        fundo.desenho(tela)
        tela.blit(texto_WIN,(320,200))
        marioWin.desenho(tela)
    pygame.display.update()
    clock.tick(60)
    
