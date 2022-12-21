import pygame
import settings
from settings import *
from Character import *
from physics import *

player = None
objects_list = []


def create_player(init_pos):
    global player, objects_list
    player = Character(pos=init_pos, size=20, color=RED)
    objects_list.append(player)
    #if player is None:
    #    print('Player already exists')
    #else:



def create_enemy(init_pos):
    global objects_list
    npc = Character(pos=init_pos, size=20, color=BLUE)
    objects_list.append(npc)
    return npc

def main():
    global objects_list, player
    create_player(Vector2D(200, 300))
    delta_pos = 0
    for i in range(4):
        e = create_enemy(Vector2D(100, 100+delta_pos))
        e.speed = Vector2D(2, 0)
        delta_pos += 50

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Hotline Miami')
    clock = pygame.time.Clock()
    player_dir = Vector2D(0, 0)
    while True:
        player_dir = Vector2D(0, 0)
        # Логика
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player_dir = Vector2D.sum(player_dir, Vector2D(-2, 0))
        if keys[pygame.K_d]:
            player_dir = Vector2D.sum(player_dir, Vector2D(2, 0))
        if keys[pygame.K_w]:
            player_dir = Vector2D.sum(player_dir, Vector2D(0, -2))
        if keys[pygame.K_s]:
            player_dir = Vector2D.sum(player_dir, Vector2D(0, 2))

        player.speed = player_dir
        for obj in objects_list:
            obj.update()
            for obj2 in objects_list:
                if obj == obj2:
                    continue
                else:
                    while CircleCollider.is_intersects(\
                            obj.collider, obj2.collider):
                        obj.speed = Vector2D.scalar_mult(obj.speed, -1)
                        obj2.speed = Vector2D.scalar_mult(obj2.speed, -1)
                        obj.move()
                        obj2.move()
        # Отрисовка
        screen.fill(WHITE)
        for o in objects_list:
            pygame.draw.circle(screen, o.sprite, (o.pos.X, o.pos.Y), o.collider.radius)
        pygame.display.flip()
        clock.tick(FPS)


main()
