import pygame
import time
import random

pygame.font.init()

display_width = 1500
display_height = 1000
square_size = display_height / 5
border_size = square_size / 20
tile_size = square_size - (2 * border_size)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
dark_grey = (30,30,30)
grey = (77, 77, 77)
red = (204, 0, 0)
green = (77, 204, 0)
blue = (0, 204, 255)
purple = (77, 0, 204)
pink = (255, 77, 255)
orange = (255, 135, 0)
yellow = (255, 255, 0)

health = 0
stats = [0,0,0,0,0]
color = [blue, purple, pink, orange, yellow]
label = ["Statistic", 'Statistic', 'Statistic', 'Statistic', 'Statistic']
name = ['Name 1', 'Name 2', 'Name 3', 'Name 4', 'Name 5']
currentCoordinates = [1,1]
oldCoordinates = [0,0]

profile = pygame.image.load('profile.png')
sprite = pygame.image.load('playerTemp.png')

def coordinates(x,y):
    return (50 + (200*(x-1)), 50 + 200*(y-1))

def generate_stats():
    global health, stats
    health = 100

    for i in range(5):
        stats[i] = random.randint(1,10)
    

def draw_board():
    gameDisplay.fill(black)
    
    for y in range(0, 5):
        for x in range(0, 5):
            pygame.draw.rect(gameDisplay, dark_grey, [x * square_size + border_size, y * square_size + border_size, tile_size, tile_size])

def draw_stats():
    pygame.draw.rect(gameDisplay, dark_grey, [display_height + border_size, border_size, display_width - display_height - (2*border_size), display_height - (2*border_size)])
    pygame.draw.rect(gameDisplay, black, [display_height + (2*border_size), 2*border_size, display_width - display_height - (4*border_size), display_width - display_height - (4*border_size)])

    for i in range(1, 6):
        myfont = pygame.font.SysFont('Arial', 22)
        textsurface = myfont.render(label[i-1] + ':  ' + str(stats[i-1]), False, grey)
        gameDisplay.blit(textsurface, (1060, 595 + (i*60)))

        pygame.draw.rect(gameDisplay, color[i-1], [1190, 600 + (i*60), 27 * stats[i-1], 20])

def draw_health():


    pygame.draw.rect(gameDisplay, red, [1040, 560, 420, 20])
    pygame.draw.rect(gameDisplay, green, [1040, 560, 4.2 * health, 20])

def draw_character_stat():
    myfont = pygame.font.SysFont('Arial', 34)
    textsurface = myfont.render(name[random.randint(0,4)], False, grey)
    gameDisplay.blit(textsurface, (1200, 40))

    gameDisplay.blit(profile, (1050, 80))

    gameDisplay.blit(sprite, coordinates(currentCoordinates[0], currentCoordinates[1]))

#This function is called when the robot begins moving, and should return when
#it notices a change in colour, with the colour detected.
#For now, just returns a random colour.
def get_colour_from_robot():
    return color[random.randint(0,4)]

def player_move(direction):
    if direction == "left":
        if currentCoordinates[0] != 1:
            oldCoordinates[0] = currentCoordinates[0]
            currentCoordinates[0] = currentCoordinates[0] - 1
    elif direction == "right":
        if currentCoordinates[0] != 5:
            oldCoordinates[0] = currentCoordinates[0]
            currentCoordinates[0] = currentCoordinates[0] + 1
    elif direction == "up":
        if currentCoordinates[1] != 5:
            oldCoordinates[1] = currentCoordinates[1]
            currentCoordinates[1] = currentCoordinates[1] - 1
    elif direction == "down":
        if currentCoordinates[1] != 1:
            oldCoordinates[1] = currentCoordinates[1]
            currentCoordinates[1] = currentCoordinates[1] + 1

def redraw_player(x,y,xold,yold):
    pygame.draw.rect(gameDisplay, dark_grey, [xold * square_size + border_size, yold * square_size + border_size, tile_size, tile_size])
    gameDisplay.blit(sprite, coordinates(x,y))

def game_loop():

    gameExit = False
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #player movement
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player_move("left")
                elif event.key == pygame.K_RIGHT:
                    player_move("right")
                elif event.key == pygame.K_UP:
                    player_move("up")
                elif event.key == pygame.K_DOWN:
                    player_move("down")

        redraw_player(currentCoordinates[0], currentCoordinates[1], oldCoordinates[0], oldCoordinates[1])
        pygame.display.update()
        clock.tick(60)


generate_stats()
draw_board()
draw_stats()
draw_health()
draw_character_stat()
game_loop()
pygame.quit()
quit()