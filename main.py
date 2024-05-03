import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("tileterpy")

tile_list = []
# TODO: load all images in /tiles
tile_list.append(pygame.image.load("tiles/grass.png"))
tile_list.append(pygame.image.load("tiles/water.png"))


def _quit():
    pygame.quit()
    sys.exit()


def draw_tile(pos):
    x = pos[0] % 32
    y = pos[1] % 32
    rect = pygame.Rect(pos[0] - x, pos[1] - y, 32, 32)
    screen.blit(tile_list[tile_index], rect)
    pygame.display.flip()


clock = pygame.time.Clock()
tile_index = 0
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            elif event.key == pygame.K_DOWN:
                tile_index -= 1
            elif event.key == pygame.K_UP:
                tile_index += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                draw_tile(pygame.mouse.get_pos())
