import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCALE = 100


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Hotline Miami')
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (100, 100, SCALE, 2*SCALE))
        pygame.display.flip()
        clock.tick(FPS)

main()