import pygame
import random

# Initialisierung von Pygame
pygame.init()

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Bildschirmgröße
WIDTH = 600
HEIGHT = 600
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

# Titel des Fensters
pygame.display.set_caption("Tic Tac Toe")

# Feldergröße
FIELD_SIZE = 200

# Spielfeld
board = [[' ' for _ in range(3)] for _ in range(3)]

# Spieler
HUMAN = 'X'
COMPUTER = 'O'

# Funktion zum Zeichnen des Spielfelds
def draw_board():
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * FIELD_SIZE), (WIDTH, i * FIELD_SIZE), 5)
        pygame.draw.line(screen, BLACK, (i * FIELD_SIZE, 0), (i * FIELD_SIZE, HEIGHT), 5)
    for i in range(3):
        for j in range(3):
            center = (j * FIELD_SIZE + FIELD_SIZE // 2, i * FIELD_SIZE + FIELD_SIZE // 2)
            if board[i][j] == HUMAN:
                pygame.draw.line(screen, BLACK, (center[0] - 80, center[1] - 80), (center[0] + 80, center[1] + 80), 5)
                pygame.draw.line(screen, BLACK, (center[0] + 80, center[1] - 80), (center[0] - 80, center[1] + 80), 5)
            elif board[i][j] == COMPUTER:
                pygame.draw.circle(screen, BLACK, center, 80, 5)

# Funktion zum Überprüfen auf Gewinn
def check_win(player):
    # Überprüfen der Reihen
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # Überprüfen der Spalten
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    # Überprüfen der Diagonalen
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

# Funktion zum Überprüfen auf Unentschieden
def check_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

# Min-Max-Algorithmus
def minimax(depth, is_maximizing):
    if check_win(COMPUTER):
        return 1
    if check_win(HUMAN):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = COMPUTER
                    score = minimax(depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = HUMAN
                    score = minimax(depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Funktion für den Computerzug
def computer_move():
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = COMPUTER
                score = minimax(0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = COMPUTER

# Spiel-Loop
running = True
game_over = False
current_player = HUMAN
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if current_player == HUMAN:
                x, y = pygame.mouse.get_pos()
                row = y // FIELD_SIZE
                col = x // FIELD_SIZE
                if board[row][col] == ' ':
                    board[row][col] = HUMAN
                    current_player = COMPUTER
    if check_draw():
        print("Unentschieden!")
        game_over = True
        
    elif check_win(HUMAN):
        print("Du hast gewonnen!")
        game_over = True

    elif check_win(COMPUTER):
        print("Der Computer hat gewonnen!")
        game_over = True

    if current_player == COMPUTER and not game_over:
        computer_move()
        current_player = HUMAN

    draw_board()
    
    

    pygame.display.flip()

pygame.quit()