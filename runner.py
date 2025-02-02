import pygame
import sys
import random
import tictactoe as ttt

# intro
pygame.init()

# Increase the window size to handle larger titles
size = width, height = 800, 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray=(80,80,80)
red=(110,0,0)
green=(0,110,0)
yellow=(150,150,0)


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe")

mediumFont = pygame.font.Font(r"C:\Users\Kiro\Desktop\pythonProject\pythonProject\OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font(r"C:\Users\Kiro\Desktop\pythonProject\pythonProject\OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font(r"C:\Users\Kiro\Desktop\pythonProject\pythonProject\OpenSans-Regular.ttf", 60)

user = None
board = ttt.initial_state()
ai_turn = False

rps_winner = None  # Track RPS winner
ai_choice = None   # Track AI's choice of X or O

# Show the welcome screen that asks the player to press any key to start
def welcome_screen():
    while True:
        #screen.fill(gray)
        background_image = pygame.image.load(r"C:\Users\Kiro\Desktop\pythonProject\pythonProject\ttt1.jpeg")  # Replace with your image path
        background_image = pygame.transform.scale(background_image, (width, height))  # Resize the image to fit the screen
        screen.blit(background_image, (0, 0))
        #welcome_text = largeFont.render("Welcome to Tic-Tac-Toe", True, white)
        #welcome_rect = welcome_text.get_rect(center=(width / 2, height / 2 - 30))
      #  screen.blit(welcome_text, welcome_rect)

        instruction_text = largeFont.render("Press any key to start", True, white)
        instruction_rect = instruction_text.get_rect(center=(width/2 , height/2  +220))
        screen.blit(instruction_text, instruction_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return  # Exit the welcome screen and start the game


def countdown_message(message, countdown_time):
    """
    Displays a message with a countdown timer.
    """
    start_ticks = pygame.time.get_ticks()
    while True:
        screen.fill(gray)

        # Calculate remaining time
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        remaining_time = max(0, countdown_time - elapsed_time)

        # Display message
        message_text = largeFont.render(message, True, white)
        message_rect = message_text.get_rect(center=(width / 2, height / 2 - 30))
        screen.blit(message_text, message_rect)

        # Display countdown timer
        timer_text = mediumFont.render(f"Starting in {int(remaining_time)} seconds...", True, white)
        timer_rect = timer_text.get_rect(center=(width / 2, height / 2 + 30))
        screen.blit(timer_text, timer_rect)

        pygame.display.flip()

        if remaining_time <= 0:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

###############################
                #RPS
def play_rps_gui():
    """
    Implements the RPS game in the GUI and determines the winner.
    """
    global rps_winner, ai_choice

    choices = ["rock", "paper", "scissors"]
    user_choice = None
    ai_rps_choice = random.choice(choices)
    display_result = None

    while rps_winner is None:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(gray)

        # Display title
        title = largeFont.render("Rock-Paper-Scissors", True, white)
        titleRect = title.get_rect(center=(width / 2, 50))
        screen.blit(title, titleRect)

        # Display choices
        button_width, button_height = 150, 60

        rockButton = pygame.Rect((width / 8), (height / 2), button_width, button_height)
        paperButton = pygame.Rect((3 * (width / 8)), (height / 2), button_width, button_height)
        scissorsButton = pygame.Rect((5 * (width / 8)), (height / 2), button_width, button_height)

        pygame.draw.rect(screen, white, rockButton)
        pygame.draw.rect(screen, white, paperButton)
        pygame.draw.rect(screen, white, scissorsButton)

        rock = mediumFont.render("Rock", True, black)
        paper = mediumFont.render("Paper", True, black)
        scissors = mediumFont.render("Scissors", True, black)

        screen.blit(rock, rock.get_rect(center=rockButton.center))
        screen.blit(paper, paper.get_rect(center=paperButton.center))
        screen.blit(scissors, scissors.get_rect(center=scissorsButton.center))

        # Display result
        if display_result:
            result_text = mediumFont.render(display_result, True, white)
            result_rect = result_text.get_rect(center=(width / 2, height - 100))
            screen.blit(result_text, result_rect)

        # Detect clicks
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if rockButton.collidepoint(mouse):
                user_choice = "rock"
            elif paperButton.collidepoint(mouse):
                user_choice = "paper"
            elif scissorsButton.collidepoint(mouse):
                user_choice = "scissors"

            if user_choice:
                # Determine winner
                if user_choice == ai_rps_choice:
                    display_result = f"AI chose {ai_rps_choice}. It's a tie!"
                    user_choice = None
                    ai_rps_choice = random.choice(choices)
                elif (user_choice == "rock" and ai_rps_choice == "scissors") or \
                     (user_choice == "paper" and ai_rps_choice == "rock") or \
                     (user_choice == "scissors" and ai_rps_choice == "paper"):
                    rps_winner = "user"
                    display_result = f"AI chose {ai_rps_choice}. You win!"
                else:
                    rps_winner = "ai"
                    display_result = f"AI chose {ai_rps_choice}. AI wins!"

        pygame.display.flip()
        pygame.time.wait(50)

 #result screen of the winner from RPS
def show_result_screen(message, display_time):
    """
    Displays a message for a fixed time before continuing.
    """
    start_ticks = pygame.time.get_ticks()
    while True:
        screen.fill(gray)

        # Display result message
        message_text = largeFont.render(message, True, white)
        message_rect = message_text.get_rect(center=(width / 2, height / 2))
        screen.blit(message_text, message_rect)

        pygame.display.flip()

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time >= display_time:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

###############################
# draw GUI of board

tiles=[]
def draw_board():
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)
# Show welcome screen
welcome_screen()
# Show countdown message
countdown_message("Get ready to play Rock-Paper-Scissors!", 3)

# Play RPS
play_rps_gui()

# Show result message of RPS
if rps_winner == "user":
    show_result_screen("You won! Choose X or O.", 1.5)
    user = None
    ai_choice = None
else:
    show_result_screen("AI won! AI will choose X or O.", 1.5)
    user = ttt.O  # AI automatically chooses X
    ai_turn = True


##########################

# Let the winner choose X or O and start the game
while True:
    tiles=[]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(gray)

    # If the user won, let them choose X or O
    if rps_winner == "user" and user is None:
        # Choice buttons for user
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)

        pygame.draw.rect(screen, white, playXButton)
        pygame.draw.rect(screen, white, playOButton)

        playX = mediumFont.render("Play as X", True, black)
        playO = mediumFont.render("Play as O", True, black)

        screen.blit(playX, playX.get_rect(center=playXButton.center))
        screen.blit(playO, playO.get_rect(center=playOButton.center))

        # Handle clicks
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                user = ttt.X
            elif playOButton.collidepoint(mouse):
                user = ttt.O

    else:
        # Existing game logic for board rendering, moves, etc.
        draw_board()
        # Check if the game is over
        game_over = ttt.terminal(board)
        current_player = ttt.player(board)

        # Display status
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                status = "Game Over: It's a tie!" 
                screen.fill(yellow)               
                
            else:
                status = f"Game Over: {winner} wins!"  
                if not ai_turn:
                    screen.fill(red)
                else:
                    screen.fill(green)

        elif user == current_player:
            status = f"Your turn ({user})"
        else:
            status = "AI thinking..."
        status_text = mediumFont.render(status, True, white)
        status_rect = status_text.get_rect(center=(width / 2, 30))
        screen.blit(status_text, status_rect)

        draw_board()
        
        ############################

        # Handle AI's turn
        if not game_over and user != current_player:
            if ai_turn:
                pygame.time.wait(300)  # Delay for AI move
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Handle user's move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == current_player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                        board = ttt.result(board, (i, j))
        

        # Handle game restart
        if game_over:
            restart_button = pygame.Rect(width / 3, height - 65, width / 3, 50)
            restart_text = mediumFont.render("Play Again", True, black)
            restart_rect = restart_text.get_rect(center=restart_button.center)
            pygame.draw.rect(screen, white, restart_button)
            screen.blit(restart_text, restart_rect)

            # Restart if clicked
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse):
                    user = None
                    rps_winner = None
                    ai_choice = None
                    board = ttt.initial_state()
                    ai_turn = False
                    countdown_message("Get ready to play Rock-Paper-Scissors!", 3)
                    play_rps_gui()
                    if rps_winner == "user":
                        show_result_screen("You won! Choose X or O.", 1.5)
                    else:
                        show_result_screen("AI won! AI will choose X or O.", 1.5)
                        user = ttt.O
                        ai_turn = True

    pygame.display.flip()
