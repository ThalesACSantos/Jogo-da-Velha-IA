import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 350
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da Velha")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CREAM = (255, 253, 208)

# Tamanho das células
CELL_SIZE = 100
BUTTON_HEIGHT = 50

game_over = False
player_score = 0  # Initialize player score
computer_score = 0  # Initialize computer score

global board  # Declare board globally

board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize board

# Função para desenhar o texto da pontuação
def draw_score(player_score, computer_score):
    font = pygame.font.Font(None, 24)
    player_text = font.render("Jogador: " + str(player_score), True, BLACK)
    computer_text = font.render("IA: " + str(computer_score), True, BLACK)
    screen.blit(player_text, (10, 300))  # Player score on left
    screen.blit(computer_text, (SCREEN_WIDTH - computer_text.get_width() - 10, 300))  # Computer score on right

def reiniciar_jogo():
    """Reinicia o jogo, limpando o tabuleiro e redefinindo as variáveis."""
    global board, game_over  # Reset both board and game_over
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False  # Set game_over back to False

# Função para desenhar o tabuleiro
def draw_board(board):
    draw_score(player_score, computer_score)
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, BLACK, (i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
            if board[i][j] == 'X':
                pygame.draw.line(screen, BLUE, (i*CELL_SIZE+15, j*CELL_SIZE+15), (i*CELL_SIZE+85, j*CELL_SIZE+85), 5)
                pygame.draw.line(screen, BLUE, (i*CELL_SIZE+15, j*CELL_SIZE+85), (i*CELL_SIZE+85, j*CELL_SIZE+15), 5)
            elif board[i][j] == 'O':
                pygame.draw.circle(screen, RED, (i*CELL_SIZE+50, j*CELL_SIZE+50), 40, 5)


# Funções para verificar vitória
def is_winner(board, player):
    # Verifica linhas, colunas e diagonais para verificar se um jogador venceu
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Função para verificar se o tabuleiro está cheio
def is_full(board):
    # Verifica se o tabuleiro está cheio
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# Função para verificar células vazias
def get_empty_cells(board):
    # Retorna uma lista de coordenadas das células vazias
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells


def minimax(board, depth, is_maximizing, player):
    """
    Implementa o algoritmo Minimax para encontrar a melhor jogada.

    Args:
        board: O tabuleiro do jogo.
        depth: A profundidade atual da busca.
        is_maximizing: Indica se é o turno do jogador que maximiza (IA) ou minimiza (usuário).
        player: O jogador atual ('X' ou 'O').

    Returns:
        O valor da melhor jogada encontrada.
    """

    # Caso base: jogo acabou
    if is_winner(board, 'X'):
        return -1  # Vitória do jogador X
    elif is_winner(board, 'O'):
        return 1  # Vitória do jogador O
    elif is_full(board):
        return 0 # Empate


    # Maximizar para o jogador da máquina (O)
    if is_maximizing:
        best_val = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = player
                    val = minimax(board, depth + 1, False, 'X')
                    board[row][col] = ' '
                    best_val = max(best_val, val)
        return best_val

    # Minimizar para o jogador humano (X)
    else:
        best_val = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = player
                    val = minimax(board, depth + 1, True, 'O')
                    board[row][col] = ' '
                    best_val = min(best_val, val)
        return best_val


def find_best_move(board):
    """
    Encontra a melhor jogada para o jogador 'O'.

    Args:
        board: O tabuleiro do jogo.

    Returns:
        Um tuplo (row, col) representando a melhor jogada.
    """

    best_val = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                move_val = minimax(board, 0, False, 'X')
                board[row][col] = ' '
                if move_val is not None and move_val > best_val:  # Check for None
                    best_val = move_val
                    best_move = (row, col)
    return best_move

    # Função para desenhar uma linha para indicar a vitória

def draw_winner_line(board, player):
    """Desenha uma linha para indicar a vitória."""
    for i in range(3):
        # Verifica linhas
        if all(board[j][i] == player for j in range(3)):
            pygame.draw.line(screen, YELLOW, (0, i * CELL_SIZE + CELL_SIZE // 2),
                             (SCREEN_WIDTH, i * CELL_SIZE + CELL_SIZE // 2), 5)
            return
        # Verifica colunas
        if all(board[i][j] == player for j in range(3)):
            pygame.draw.line(screen, YELLOW, (i * CELL_SIZE + CELL_SIZE // 2, 0),
                             (i * CELL_SIZE + CELL_SIZE // 2, SCREEN_HEIGHT - BUTTON_HEIGHT), 5)
            return
    # Verifica diagonais
    if all(board[i][i] == player for i in range(3)):
        pygame.draw.line(screen, YELLOW, (0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT - BUTTON_HEIGHT), 5)
        return
    if all(board[i][2 - i] == player for i in range(3)):
        pygame.draw.line(screen, YELLOW, (0, SCREEN_HEIGHT - BUTTON_HEIGHT), (SCREEN_WIDTH, 0), 5)
        return

def update_score(winner):
    """Atualiza a pontuação do jogador vencedor."""
    global player_score, computer_score
    if winner == 'X':
        player_score += 1
    elif winner == 'O':
        computer_score += 1
    #game_over = False

# Criando o botão de reiniciar (exemplo usando pygame.Rect centralizado))

button_width = 100
button_height = 50
button_x = (SCREEN_WIDTH - button_width) // 2
button_y = SCREEN_HEIGHT - BUTTON_HEIGHT
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
font = pygame.font.Font(None, 26)
button_text = font.render("Reiniciar", True, BLACK)

# Função para desenhar o botão
def draw_button():
    pygame.draw.rect(screen, GRAY, button_rect)
    screen.blit(button_text, (button_x + 10, button_y + 10))

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Processar apenas eventos de clique do mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Verificar se o clique foi dentro do tabuleiro
            if 0 <= mouse_x < SCREEN_WIDTH and 0 <= mouse_y < SCREEN_HEIGHT - BUTTON_HEIGHT:
                # Calcular a coluna e a linha (note a inversão)
                col = mouse_y // CELL_SIZE
                row = mouse_x // CELL_SIZE

                # Verificar se a célula está vazia e se é a vez do jogador
                if board[row][col] == ' ' and not game_over:
                    board[row][col] = 'X'

                    if not is_full(board):
                        # Jogada da IA
                        row, col = find_best_move(board)
                        if row != -1 and col != -1:
                            board[row][col] = 'O'

                    # Verificar se o jogo acabou
                    if is_winner(board, 'X') or is_winner(board, 'O') or is_full(board):
                        game_over = True

            # Verificar se o botão foi clicado
            elif button_rect.collidepoint(mouse_x, mouse_y):
                reiniciar_jogo()

    # Desenhar a tela
    #screen.fill(BLACK)
    screen.fill(CREAM)

    # Desenhar o botão
    draw_button()

    # Desenhar o tabuleiro e as peças
    draw_board(board)

    # atualizar a tela
    pygame.display.flip()

    # Desenhar a linha de vitória, se houver
    if game_over:
        if is_winner(board, 'X'):
            draw_winner_line(board, 'X')
            update_score('X')
        elif is_winner(board, 'O'):
            draw_winner_line(board, 'O')
            update_score('O')
        draw_score(player_score, computer_score)  # Desenhe a pontuação após a vitória
        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(1000)  # Pausa de 2 segundos antes de reiniciar
        pygame.time.delay(1000)  # Pausa de 2 segundos antes de reiniciar
        reiniciar_jogo()  # Reinicia o jogo após a pausa

        #draw_winner_line(board, 'X' if is_winner(board, 'X')) else 'O')
        #if is_winner(board, 'X'):
    pygame.display.flip()
    pygame.display.update()

pygame.quit()