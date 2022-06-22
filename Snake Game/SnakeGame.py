import pygame
import time
import random
 
pygame.init() 

#Color Score
colorScore = (255,255,255)
#Color Snake
colorSnake = (57, 255, 20)
#Color Msg GameOver
colorMsgGameOver = (255,0,0)
#Target Color
colorTarget = (255,0,0)
#background Color
colorBackground = (0,0,0)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snakeBlock = 10
snakeSpeed = 17
 
fontStyle = pygame.font.SysFont("modernno20", 25)
scoreFont = pygame.font.SysFont("modernno20", 15)
 
#score
def score(score):
    value = scoreFont.render("Score: " + str(score), True, colorScore)
    dis.blit(value, [0, 0])

#snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,colorSnake, [x[0], x[1], snake_block, snake_block])
#message
def messageGameOver(msg, color):
    mesg = fontStyle.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    snakeLength = 1
 
    targetX = round(random.randrange(0, dis_width - snakeBlock) / 10.0) * 10.0
    targetY = round(random.randrange(0, dis_height - snakeBlock) / 10.0) * 10.0
 
    while not game_over:
        while game_close == True:
            dis.fill(colorBackground)
            messageGameOver("Game Over! Press (P)Play Again or (Q)Quit", colorMsgGameOver)
            score(snakeLength - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snakeBlock
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snakeBlock
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(colorBackground)
        pygame.draw.rect(dis,colorTarget, [targetX, targetY, snakeBlock, snakeBlock])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snakeLength:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        snake(snakeBlock, snake_List)
        score(snakeLength - 1)
 
        pygame.display.update()
 
        if x1 == targetX and y1 == targetY:
            targetX = round(random.randrange(0, dis_width - snakeBlock) / 10.0) * 10.0
            targetY = round(random.randrange(0, dis_height - snakeBlock) / 10.0) * 10.0
            snakeLength += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()
 
gameLoop()