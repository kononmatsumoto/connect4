import pygame
from constants import *
from board import *

def draw_board(screen, board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (c*SQUARESIZE + SQUARESIZE//2, (r+1)*SQUARESIZE + SQUARESIZE//2), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c*SQUARESIZE + SQUARESIZE//2, HEIGHT - (r*SQUARESIZE + SQUARESIZE//2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE + SQUARESIZE//2, HEIGHT - (r*SQUARESIZE + SQUARESIZE//2)), RADIUS)
    pygame.display.update()

def run_game():
    board = create_board()
    game_over = False
    turn = 0

    screen = pygame.display.set_mode(SIZE)
    font = pygame.font.SysFont("monospace", 75)
    draw_board(screen, board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                pygame.draw.circle(screen, RED if turn == 0 else YELLOW, (posx, SQUARESIZE//2), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                col = event.pos[0] // SQUARESIZE

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    piece = 1 if turn == 0 else 2
                    drop_piece(board, row, col, piece)

                    if winning_move(board, piece):
                        label = font.render(f"Player {piece} wins!", 1, RED if piece == 1 else YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

                    draw_board(screen, board)
                    turn ^= 1

                if game_over:
                    pygame.time.wait(3000)
