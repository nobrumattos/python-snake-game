import pygame
import time
import random

# Inicializar o pygame
pygame.init()

# Definir as cores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Definir o tamanho da tela
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Jogo da Cobra')

# Configurações do relógio
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 20

# Função para desenhar a cobra
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Função para exibir a mensagem de fim de jogo
def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    words = msg.split(' ')
    lines = []
    line = ''
    for word in words:
        test_line = line + word + ' '
        test_surface = font_style.render(test_line, True, color)
        if test_surface.get_width() > dis_width * 0.8:  # se a linha exceder 80% da largura da tela
            lines.append(line)
            line = word + ' '
        else:
            line = test_line
    lines.append(line)  # Adiciona a última linha
    y_offset = dis_height / 3
    for line in lines:
        mesg = font_style.render(line, True, color)
        dis.blit(mesg, [dis_width / 6, y_offset])
        y_offset += 60  # espaço entre as linhas

# Função para desenhar o placar
def your_score(score):
    font_style = pygame.font.SysFont(None, 50)
    value = font_style.render("Pontuação: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Função para a tela inicial
def game_intro():
    intro = True
    while intro:
        dis.fill(blue)
        font_style = pygame.font.SysFont(None, 75)
        intro_text = font_style.render("Jogo da Cobra", True, yellow)
        dis.blit(intro_text, [dis_width / 6, dis_height / 3])
        
        large_text = pygame.font.SysFont(None, 50)
        instructions = large_text.render("Pressione C para Jogar ou Q para Sair", True, white)
        dis.blit(instructions, [dis_width / 6, dis_height / 2])
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False

# Função principal do jogo
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Você perdeu! Pressione Q para sair ou C para jogar novamente", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Inicie a tela inicial
game_intro()

# Inicie o jogo
gameLoop()
