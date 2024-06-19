import pygame
from chess_piece import get_legal_moves

BOARD_SIZE = 8
SQUARE_SIZE = 80
LIGHT_BROWN = (222, 184, 135)
DARK_BROWN = (139, 69, 19)
HIGHLIGHT_COLOR = (0, 255, 0, 100)

class ChessBoard:
    def __init__(self):
        self.board = [
            ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
        ]
        self.pieces = {}
        self.move_history = []
        self.redo_stack = []
        self.turn = 'w'

    def load_images(self):
        for piece in ['wp', 'bp', 'wn', 'bn', 'wb', 'bb', 'wr', 'br', 'wq', 'bq', 'wk', 'bk']:
            self.pieces[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE))

    def draw_board(self, screen):
        colors = [LIGHT_BROWN, DARK_BROWN]
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = colors[(row + col) % 2]
                pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board[row][col]
                if piece != '--':
                    screen.blit(self.pieces[piece], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move_piece(self, start, end):
        piece = self.board[start[1]][start[0]]
        self.board[start[1]][start[0]] = '--'
        captured_piece = self.board[end[1]][end[0]]
        self.board[end[1]][end[0]] = piece
        self.move_history.append((start, end, piece, captured_piece))
        self.redo_stack.clear()
        self.turn = 'b' if self.turn == 'w' else 'w'

    def undo_move(self):
        if self.move_history:
            start, end, piece, captured_piece = self.move_history.pop()
            self.board[end[1]][end[0]] = captured_piece
            self.board[start[1]][start[0]] = piece
            self.redo_stack.append((start, end, piece, captured_piece))
            self.turn = 'b' if self.turn == 'w' else 'w'

    def redo_move(self):
        if self.redo_stack:
            start, end, piece, captured_piece = self.redo_stack.pop()
            self.board[start[1]][start[0]] = '--'
            self.board[end[1]][end[0]] = piece
            self.move_history.append((start, end, piece, captured_piece))
            self.turn = 'b' if self.turn == 'w' else 'w'

    def get_legal_moves(self, square):
        x, y = square
        piece = self.board[y][x]
        if piece == '--' or piece[0] != self.turn:
            return []
        return get_legal_moves(self.board, x, y)

    def draw_highlighted_squares(self, screen, squares):
        surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        surface.fill(HIGHLIGHT_COLOR)
        for (x, y) in squares:
            screen.blit(surface, (x * SQUARE_SIZE, y * SQUARE_SIZE))
