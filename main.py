from constants import *
import pygame

def main():
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, pygame.Color(0,0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
