import pygame
import random

class Objetivos:
    def __init__(self,arquivo_da_img,alturaIMG,larguraIMG,x_inicial,y_inicial, velocidade) -> None:
        self.imagem = pygame.image.load(arquivo_da_img)
        
        self.largura = larguraIMG
        self.altura = alturaIMG

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial
        self.velocidade = velocidade    
        self.mascara = pygame.mask.from_surface(self.imagem)
    
    def desenho(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))

    def velocidades(self):
        velocidade = random.randint(1,10)
        return velocidade
    
    def movimento_obj(self):
        self.pos_y += self.velocidade
        if self.pos_y >800:
            self.pos_y =0