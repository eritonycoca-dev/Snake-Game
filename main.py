import pygame
import sys 
from settings import WIDTH, HEIGHT, BLACK, GREEN, WHITE, RED     
from snake import Snake 
from food import Food 
from obstacles import Obstacles  

def load_highscore():
    try:
        with open("highscore.txt", "r") as f: 
            return int(f.read()) 
    except:
        return 0
    
def save_highscore(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

def main():

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Jungle Edition")

    clock = pygame.time.Clock()

    background = pygame.image.load("assets/jungle_bg.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    eat_sound = pygame.mixer.Sound("assets/eat.wav") 
    game_over_sound = pygame.mixer.Sound("assets/game_over.wav")

    font = pygame.font.SysFont("arial", 28)
    big_font = pygame.font.SysFont("arial", 40)

    highscore = load_highscore()

    # MENÚ 
    player_name= ""
    menu=True 

    while menu: 
        screen.fill(BLACK)

        title = big_font.render("BIENVENIDO A SNAKE JUNGLE", True, GREEN)
        
        rules1 = font.render("Reglas del juego:", True, WHITE)
        rules2 = font.render("1. Si chocas con tu cuerpo o los bordes, perderás", True, WHITE)
        rules3 = font.render("2. Los ratones te dan puntos y te harán crecer.", True, WHITE)
        rules4 = font.render("3. Controla tu serpiente con las flechas del teclado", True, WHITE)

        name_text = font.render(f"Nombre de tu serpiente: {player_name}", True, WHITE)
        start_text = font.render("Presiona ENTER para comenzar", True, WHITE)

        screen.blit(title, (WIDTH//2 - 250, 80))
        screen.blit(rules1, (100, 150))
        screen.blit(rules2, (100, 190))
        screen.blit(rules3, (100, 220))
        screen.blit(rules4, (100, 250))
        screen.blit(name_text, (100, 320))
        screen.blit(start_text, (100, 360))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_name != "":
                    menu= False 
                elif event.key == pygame.K_BACKSPACE: 
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode
    
    snake = Snake(player_name)
    obstacles = Obstacles(snake.body)
    food = Food(snake.body, obstacles.positions)

    score = 0
    running = True 

    while running: 

        clock.tick(snake.speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        snake.move()

        head = snake.body[0]

        #COLISIONES
        if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or 
            snake.check_self_collision() or 
            head in obstacles.positions):
            game_over_sound.play()
            running = False 

        if head == food.position: 
            eat_sound.play()
            snake.grow_snake()
            score += 2
            food = Food(snake.body, obstacles.positions)

        screen.blit(background, (0,0))
        obstacles.draw(screen)
        snake.draw(screen)
        food.draw(screen)

        score_text = font.render(f"Score: {score}", True, WHITE)
        high_text = font.render(f"Record: {highscore}", True, WHITE)
        name_display = font.render(f"Jugador: {player_name}", True, WHITE)

        screen.blit(score_text, (10,10))
        screen.blit(high_text, (10,40))
        screen.blit(name_display, (10,70))

        pygame.display.update()

    # PANTALLA FINAL 
    if score > highscore:
        save_highscore(score)

    over=True 
    while over:

        screen.fill(BLACK)

        text = big_font.render("¡CHOCASTE!", True, RED)
        score_final = font.render(f"Puntaje final: {score}", True, WHITE)
        restart = font.render("R para reiniciar", True, WHITE)
        exit_game = font.render("ESC para salir", True, WHITE)

        screen.blit(text, (WIDTH//2 - 120, HEIGHT//3))
        screen.blit(score_final, (WIDTH//2 - 120, HEIGHT//2))
        screen.blit(restart, (WIDTH//2 - 120, HEIGHT//2 + 40))
        screen.blit(exit_game, (WIDTH//2 - 120, HEIGHT//2 + 80))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_ESCAPE: 
                    over=False
    pygame.quit()

if __name__ == "__main__":
    main()
