import pygame
import sys
import camera
import data


def _quit():
    data.save(placed_tiles, map_size, tile_size)
    pygame.quit()
    sys.exit()


def draw_tile(pos, _placed_tiles):
    _x = pos[0] % tile_size
    _y = pos[1] % tile_size
    _tuple = pos[0] - _x, pos[1] - _y
    _placed_tiles = list(filter(lambda _t: filter_list(_t, _tuple[0], _tuple[1]), _placed_tiles))
    _placed_tiles.append(((tile_index, tile_list[tile_index]), _tuple))
    _placed_tiles = list(set(_placed_tiles))
    return _placed_tiles


def filter_list(_tuple, _x, _y):
    return (_tuple[1][0], _tuple[1][1]) != (_x, _y)


def refresh_screen():
    screen.fill((0, 0, 0))
    for tile in default_tiles:
        screen.blit(tile[0][1], camera_offset_pos((tile[1][0], tile[1][1])))

    for tile in placed_tiles:
        screen.blit(tile[0][1], camera_offset_pos((tile[1][0], tile[1][1])))
    pygame.display.flip()


def camera_negative_offset_pos(_tuple):
    return _tuple[0] - camera.get_pos()[0], _tuple[1] - camera.get_pos()[1]


def camera_offset_pos(_tuple):
    return _tuple[0] + camera.get_pos()[0], _tuple[1] + camera.get_pos()[1]


def move_camera(_x, _y):
    camera.move(_x, _y)
    refresh_screen()


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("tileterpy")

camera = camera.Camera(0, 0)

tile_size = 32  # TODO: you should be able to change this in the program

tile_list = []
# TODO: load all images in /tiles
tile_list.append(pygame.image.load("tiles/grass.png"))
tile_list.append(pygame.image.load("tiles/water.png"))

map_size = (32, 32)  # TODO: you should be able to change this in the program
default_tile = pygame.image.load("tiles/default.png")
default_tiles = []
# placed_tiles = data.load()
placed_tiles = []
for y in range(map_size[0]):
    for x in range(map_size[1]):
        default_tiles.append(((-1, default_tile), (x * tile_size, y * tile_size)))
refresh_screen()

clock = pygame.time.Clock()
tile_index = 0
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                _quit()
            elif event.key == pygame.K_DOWN:
                tile_index -= 1
            elif event.key == pygame.K_UP:
                tile_index += 1

    keys = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()

    if keys[pygame.K_a]:
        move_camera(tile_size, 0)
    if keys[pygame.K_d]:
        move_camera(-tile_size, 0)
    if keys[pygame.K_w]:
        move_camera(0, tile_size)
    if keys[pygame.K_s]:
        move_camera(0, -tile_size)
    if mouse_buttons[0]:
        placed_tiles = draw_tile(camera_negative_offset_pos(pygame.mouse.get_pos()), placed_tiles)
        refresh_screen()
