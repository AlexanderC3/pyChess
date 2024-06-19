import pygame
import sys
from chess_board import ChessBoard
from utils import get_square_under_mouse, draw_move_history

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 8 * 80 + 200, 8 * 80

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

# Initialize the board
board = ChessBoard()
board.load_images()

font = pygame.font.SysFont(None, 24)

selected_square = None
legal_moves = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            square = get_square_under_mouse()
            if square:
                if selected_square and square in legal_moves:
                    board.move_piece(selected_square, square)
                    selected_square = None
                    legal_moves = []
                else:
                    selected_square = square
                    legal_moves = board.get_legal_moves(square)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                board.undo_move()
                selected_square = None
                legal_moves = []
            elif event.key == pygame.K_r:
                board.redo_move()
                selected_square = None
                legal_moves = []

    screen.fill((255, 255, 255))
    board.draw_board(screen)
    board.draw_highlighted_squares(screen, legal_moves)
    draw_move_history(screen, board.move_history, font)
    pygame.display.flip()

pygame.quit()
sys.exit()
