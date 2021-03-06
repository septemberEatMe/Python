import sys
import pygame
from classes import Player

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('My Asleep Reflections')

class Main():
    def __init__(self,screen):
        self.screen = screen
        self.back = pygame.image.load(r'D:\Code\Python\pygame\OOP Games (my asleep reflection)\\1.jpg')
        self.player = Player()
        self.main_loop()
        
    def render(self):
        '''Отвечает за отрисовку элементов на экране'''
        self.screen.blit(self.back, (0, -300))
        self.player.render(screen)

        pygame.display.flip()
        pygame.mouse.set_visible(False)

    def main_loop(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.player.pos_x += 2
            if keys[pygame.K_a]:
                self.player.pos_x -= 2

            self.render()

            
main = Main(screen)
