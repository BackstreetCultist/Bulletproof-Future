import pygame
import time
import random
import socket
import sys

pygame.font.init()


# Networking
sock = None
client_addr = None
connection = None


# GUI

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
green = (0, 143, 17)

health = 0
stats = [0,0,0,0,0]
color = [blue, purple, pink, orange, yellow]
label = ["Statistic", 'Statistic', 'Statistic', 'Statistic', 'Statistic']
namesArr = ['Octocat', 'Octocat Pirate', 'Octocat Cowboy', 'Octocat Cyborg', 'Goth Octocat']
imgArr = ['octoCat1.png', 'octoCat2.png', 'octoCat3.png', 'octoCat4.png', 'octoCat5.png']
imgArrSmall = ['octoCat1small.png', 'octoCat2small.png', 'octoCat3small.png', 'octoCat4small.png', 'octoCat5small.png']
bosses = [0 for i in range(25)]
name = 'Test'
currentCoordinates = [1,1]
previousText = 'Welcome to the Machine.'

boss1 = pygame.image.load('goal.png')
boss2 = pygame.image.load('goal.png')
boss3 = pygame.image.load('goal.png')
b1 = (0,0)
b2 = (0,0)
b3 = (0,0)
sprite = pygame.image.load(imgArrSmall[0])

def send_movement(client):
    pass

def coordinates(x,y):
    return (50 + (200*(x-1)), 50 + 200*(y-1))

def generate_stats():
    global health, stats, namesArr, name, profile, sprite
    health = 100
    x = random.randint(0,4)
    name = namesArr[x]
    profile = pygame.image.load(imgArr[x])
    sprite = pygame.image.load(imgArrSmall[x])

    for i in range(5):
        stats[i] = random.randint(1,10)
    

def draw_board():
    gameDisplay.fill(black)
    
    for y in range(0, 5):
        for x in range(0, 5):
            pygame.draw.rect(gameDisplay, dark_grey, [x * square_size + border_size, y * square_size + border_size, tile_size, tile_size])

    gameDisplay.blit(sprite, coordinates(currentCoordinates[0], currentCoordinates[1]))
    gameDisplay.blit(boss1, coordinates(*b1))
    gameDisplay.blit(boss2, coordinates(*b2))
    gameDisplay.blit(boss3, coordinates(*b3))

def draw_stats():
    pygame.draw.rect(gameDisplay, dark_grey, [display_height + border_size, border_size, display_width - display_height - (2*border_size), display_height - (2*border_size)])
    pygame.draw.rect(gameDisplay, black, [display_height + (2*border_size), 2*border_size, display_width - display_height - (4*border_size), display_width - display_height - (4*border_size)])

    for i in range(1, 6):
        myfont = pygame.font.SysFont('Arial', 22)
        textsurface = myfont.render(label[i-1] + ':  ' + str(stats[i-1]), False, grey)
        gameDisplay.blit(textsurface, (1060, 595 + (i*40)))

        pygame.draw.rect(gameDisplay, color[i-1], [1190, 600 + (i*40), 27 * stats[i-1], 20])

def draw_health():
    pygame.draw.rect(gameDisplay, red, [1040, 560, 420, 20])
    pygame.draw.rect(gameDisplay, green, [1040, 560, 4.2 * health, 20])

def draw_character_stat():
    myfont = pygame.font.SysFont('Arial', 34)
    textsurface = myfont.render(name, False, grey)
    gameDisplay.blit(textsurface, (1160, 40))

    gameDisplay.blit(profile, (1050, 80))

def draw_text(outputText):
    global previousText

    if outputText == None:
        font = pygame.font.SysFont('Courier', 24, False, False)
        text = font.render(previousText, False, green)
        gameDisplay.blit(text, (1050, 850))
    else:
        font = pygame.font.SysFont('Courier', 24, False, False)
        text = font.render(outputText, False, green)
        gameDisplay.blit(text, (1050, 850))
        previousText = outputText

def draw_attack():
    pygame.draw.rect(gameDisplay, red, [1050, 910, 400, 60])

def generate_boss():
    boss = random.randint(1,24)
    
    while True:
        if bosses[boss] == 0:
            bosses[boss] = 1
            print(boss)
            return (boss % 5 + 1, int(boss/5)+1)
        else:
            boss = random.randint(0,24)


#This function is called when the robot begins moving, and should return when
#it notices a change in colour, with the colour detected.
#For now, just returns a random colour.
#FR THO THIS IS GONNA BE REALLY IMPORTANT
def get_colour_from_robot():
    return color[random.randint(0,4)]

def player_move(direction):
    global connection
    if direction == "left":
        if currentCoordinates[0] != 1:
            currentCoordinates[0] = currentCoordinates[0] - 1
            if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] == 1:
                draw_text('Prepare for an encounter')
    elif direction == "right":
        if currentCoordinates[0] != 5:
            currentCoordinates[0] = currentCoordinates[0] + 1
            if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] == 1:
                draw_text('Prepare for an encounter')
    elif direction == "up":
        if currentCoordinates[1] != 1:
            currentCoordinates[1] = currentCoordinates[1] - 1
            if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] == 1:
                draw_text('Prepare for an encounter')
    elif direction == "down":
        if currentCoordinates[1] != 5:
            currentCoordinates[1] = currentCoordinates[1] + 1
            if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] == 1:
                draw_text('Prepare for an encounter')

    connection.sendall(direction.encode("ascii"))
    

def game_loop():

    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #player movement
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_move("left")
                elif event.key == pygame.K_RIGHT:
                    player_move("right")
                elif event.key == pygame.K_UP:
                    player_move("up")
                elif event.key == pygame.K_DOWN:
                    player_move("down")

        draw_board()
        draw_stats()
        draw_health()
        draw_character_stat()
        draw_text(None)
        if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] == 1:
                draw_attack()
        pygame.display.update()
        clock.tick(60)


def init_connection():
    global client_addr, sock,connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_addr = ('0.0.0.0', 7777)
    print("Starting up on %s:%d"%server_addr)
    sock.bind(server_addr)

    sock.listen(1)
    print("Waiting for a connection")
    connection, client_addr  = sock.accept() 
    print("Got connection from", client_addr)


init_connection()
generate_stats()
b2 = generate_boss()
b3 = generate_boss()
draw_board()
draw_stats()
draw_health()
draw_character_stat()
draw_text('Welcome to the Machine.')
game_loop()
pygame.quit()
quit()