import pygame
import sys
import random

# إعدادات اللعبة
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
ROWS, COLS = HEIGHT // TILE_SIZE, WIDTH // TILE_SIZE

# ألوان
GRASS = (106, 190, 48)
DIRT = (151, 105, 79)
SKY = (135, 206, 235)
PLAYER = (255, 221, 77)  # لون سكن اللاعب
WOOD = (102, 51, 0)
LEAVES = (34, 139, 34)
SELECTED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Minecraft 2D Mini')
clock = pygame.time.Clock()
font = pygame.font.SysFont('consolas', 20)

# عالم الكتل (0: فراغ, 1: تراب, 2: عشب, 3: خشب, 4: أوراق)
world = [[0 for _ in range(COLS)] for _ in range(ROWS)]
for y in range(ROWS):
    for x in range(COLS):
        if y > ROWS // 2:
            world[y][x] = 1  # تراب
        elif y == ROWS // 2:
            world[y][x] = 2  # عشب

# إضافة أشجار عشوائية
for _ in range(8):
    tx = random.randint(2, COLS-3)
    ty = ROWS // 2
    world[ty-1][tx] = 3  # خشب
    world[ty-2][tx] = 3
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if not (dx == 0 and dy == 0):
                world[ty-3+dy][tx+dx] = 4  # أوراق
    world[ty-3][tx] = 4

# اللاعب
player_x, player_y = COLS // 2, ROWS // 2
player_skin = pygame.Surface((TILE_SIZE-10, TILE_SIZE-10))
player_skin.fill(PLAYER)
pygame.draw.rect(player_skin, (0,0,0), (0,0,TILE_SIZE-10,TILE_SIZE-10), 2)

# الإنفنتوري
inventory = [1, 2, 3, 4]  # تراب، عشب، خشب، أوراق
inventory_names = ['تراب', 'عشب', 'خشب', 'أوراق']
selected = 0

block_colors = {0:SKY, 1:DIRT, 2:GRASS, 3:WOOD, 4:LEAVES}

def draw_world():
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            color = block_colors.get(world[y][x], SKY)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (80,80,80), rect, 1)

def draw_player():
    rect = pygame.Rect(player_x*TILE_SIZE+5, player_y*TILE_SIZE+5, TILE_SIZE-10, TILE_SIZE-10)
    screen.blit(player_skin, rect)
    pygame.draw.rect(screen, SELECTED, rect, 2)

def draw_inventory():
    pygame.draw.rect(screen, (60,60,60), (0, HEIGHT-50, WIDTH, 50))
    for i, block in enumerate(inventory):
        rect = pygame.Rect(20+i*60, HEIGHT-45, 40, 40)
        pygame.draw.rect(screen, block_colors[block], rect)
        if i == selected:
            pygame.draw.rect(screen, SELECTED, rect, 3)
        txt = font.render(inventory_names[i], True, (255,255,255))
        screen.blit(txt, (20+i*60, HEIGHT-20))

def main():
    global player_x, player_y, selected
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= 1
                elif event.key == pygame.K_RIGHT and player_x < COLS-1:
                    player_x += 1
                elif event.key == pygame.K_UP and player_y > 0:
                    player_y -= 1
                elif event.key == pygame.K_DOWN and player_y < ROWS-1:
                    player_y += 1
                elif event.key == pygame.K_SPACE:
                    # ضع أو اكسر بلوك
                    if world[player_y][player_x] == 0:
                        world[player_y][player_x] = inventory[selected]
                    else:
                        world[player_y][player_x] = 0
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    selected = event.key - pygame.K_1
        screen.fill(SKY)
        draw_world()
        draw_player()
        draw_inventory()
        pygame.display.flip()
        clock.tick(15)

if __name__ == '__main__':
    main()
