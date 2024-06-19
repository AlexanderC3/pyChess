import pygame

SQUARE_SIZE = 80
BOARD_SIZE = 8

def get_square_under_mouse():
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x, y = [int(v // SQUARE_SIZE) for v in mouse_pos]
    if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
        return (x, y)
    return None

def draw_move_history(screen, move_history, font):
    move_list = [f"{chr(97+start[0])}{8-start[1]} -> {chr(97+end[0])}{8-end[1]}" for start, end, _, _ in move_history]
    move_list = [move_list[i:i+2] for i in range(0, len(move_list), 2)]
    moves_str = [" ".join(pair) for pair in move_list]

    y_offset = 10
    for move in moves_str:
        move_text = font.render(move, True, (0, 0, 0))
        screen.blit(move_text, (8 * SQUARE_SIZE + 10, y_offset))
        y_offset += 30
