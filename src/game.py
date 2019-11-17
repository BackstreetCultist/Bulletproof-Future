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

boss1Bool = True
boss2Bool = True
boss3Bool = True

boss1 = pygame.image.load('goal.png')
boss2 = pygame.image.load('goal.png')
boss3 = pygame.image.load('goal.png')
b1 = (0,0)
b2 = (0,0)
b3 = (0,0)
sprite = pygame.image.load(imgArrSmall[0])

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
    global boss1Bool, boss2Bool, boss3Bool
    gameDisplay.fill(black)
    
    for y in range(0, 5):
        for x in range(0, 5):
            pygame.draw.rect(gameDisplay, dark_grey, [x * square_size + border_size, y * square_size + border_size, tile_size, tile_size])

    gameDisplay.blit(sprite, coordinates(currentCoordinates[0], currentCoordinates[1]))
    if boss1Bool == True:
        gameDisplay.blit(boss1, coordinates(*b1))
    if boss2Bool == True:    
        gameDisplay.blit(boss2, coordinates(*b2))
    if boss3Bool == True:    
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
    font = pygame.font.SysFont('Courier', 24, False, False)
    text = font.render('Press Enter to Attack', False, green)
    gameDisplay.blit(text, (1050, 910))

def generate_boss(id):
    boss = random.randint(1,24)
    
    while True:
        if bosses[boss] == 0:
            bosses[boss] = id
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
    if direction == "left":
        if currentCoordinates[0] != 1:
            currentCoordinates[0] = currentCoordinates[0] - 1
            if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] != 0:
                draw_text('Prepare for an encounter')
    elif direction == "right":
        if currentCoordinates[0] != 5:
            currentCoordinates[0] = currentCoordinates[0] + 1
            if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] != 0:
                draw_text('Prepare for an encounter')
    elif direction == "up":
        if currentCoordinates[1] != 1:
            currentCoordinates[1] = currentCoordinates[1] - 1
            if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] != 0:
                draw_text('Prepare for an encounter')
    elif direction == "down":
        if currentCoordinates[1] != 5:
            currentCoordinates[1] = currentCoordinates[1] + 1
            if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] != 0:
                draw_text('Prepare for an encounter')

def attack(boss):
    global health, bosses, boss1Bool, boss2Bool, boss3Bool

    #Boss weighting - bosses get harder the fewer are left
    threshold = random.randint(1,20)
    if sum(bosses) == 3:
        threshold = threshold + 1
    elif sum(bosses) == 2:
        threshold = threshold + 3
    elif sum(bosses) == 1:
        threshold = threshold + 5
    
    #Player score calculation
    roll = random.randint(1,20)
    tileColor = get_colour_from_robot()
    if tileColor == blue:
        roll = roll + stats[0]
    elif tileColor == purple:
        roll = roll + stats[1]
    elif tileColor == pink:
        roll = roll + stats[2]
    elif tileColor == orange:
        roll = roll + stats[3]
    elif tileColor == yellow:
        roll = roll + stats[4]
    
    #What happens
    if roll > threshold:
        draw_text('Another one down.')
        
        if bosses[boss] == 1:
            boss1Bool = False
        elif bosses[boss] == 2:
            boss2Bool = False
        else:
            boss3Bool = False
        bosses[boss] = 0

    elif roll == threshold:
        draw_text('They got away. So did you.')
        generate_boss(bosses[boss])
        
    elif roll < threshold:
        draw_text('That one hurt.')
        health = health - 20
        generate_boss(bosses[boss])

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
                elif event.key == pygame.K_RETURN and (((currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1) != 0):
                    print(boss1Bool)
                    print(boss2Bool)
                    print(boss3Bool)
                    print('\n')
                    attack((currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1)

        draw_board()
        draw_stats()
        draw_health()
        draw_character_stat()
        draw_text(None)
        if bosses[(currentCoordinates[1]-1) * 5 + currentCoordinates[0] - 1] != 0:
                draw_attack()
        pygame.display.update()
        clock.tick(60)


generate_stats()
b1 = generate_boss(1)
b2 = generate_boss(2)
b3 = generate_boss(3)
draw_board()
draw_stats()
draw_health()
draw_character_stat()
draw_text('Welcome to the Machine.')
game_loop()
pygame.quit()
quit()