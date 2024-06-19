def get_pawn_moves(board, x, y, color):
    direction = -1 if color == 'w' else 1
    start_row = 6 if color == 'w' else 1
    moves = []

    # Move forward
    if board[y + direction][x] == '--':
        moves.append((x, y + direction))
        if y == start_row and board[y + 2 * direction][x] == '--':
            moves.append((x, y + 2 * direction))

    # Capture diagonally
    if x - 1 >= 0 and board[y + direction][x - 1][0] == ('b' if color == 'w' else 'w'):
        moves.append((x - 1, y + direction))
    if x + 1 < 8 and board[y + direction][x + 1][0] == ('b' if color == 'w' else 'w'):
        moves.append((x + 1, y + direction))

    return moves

def get_knight_moves(board, x, y, color):
    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    moves = []
    for dx, dy in knight_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and (board[ny][nx] == '--' or board[ny][nx][0] != color):
            moves.append((nx, ny))
    return moves

def get_rook_moves(board, x, y, color):
    moves = []

    # Horizontal and vertical moves
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        while 0 <= nx < 8 and 0 <= ny < 8:
            if board[ny][nx] == '--':
                moves.append((nx, ny))
            elif board[ny][nx][0] != color:
                moves.append((nx, ny))
                break
            else:
                break
            nx += dx
            ny += dy
    return moves

def get_bishop_moves(board, x, y, color):
    moves = []

    # Diagonal moves
    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        nx, ny = x + dx, y + dy
        while 0 <= nx < 8 and 0 <= ny < 8:
            if board[ny][nx] == '--':
                moves.append((nx, ny))
            elif board[ny][nx][0] != color:
                moves.append((nx, ny))
                break
            else:
                break
            nx += dx
            ny += dy
    return moves

def get_queen_moves(board, x, y, color):
    return get_rook_moves(board, x, y, color) + get_bishop_moves(board, x, y, color)

def get_king_moves(board, x, y, color):
    king_moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    moves = []
    for dx, dy in king_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and (board[ny][nx] == '--' or board[ny][nx][0] != color):
            moves.append((nx, ny))
    return moves

def get_legal_moves(board, x, y):
    piece = board[y][x]
    if piece == '--':
        return []
    color = piece[0]
    piece_type = piece[1]

    if piece_type == 'p':
        return get_pawn_moves(board, x, y, color)
    elif piece_type == 'n':
        return get_knight_moves(board, x, y, color)
    elif piece_type == 'r':
        return get_rook_moves(board, x, y, color)
    elif piece_type == 'b':
        return get_bishop_moves(board, x, y, color)
    elif piece_type == 'q':
        return get_queen_moves(board, x, y, color)
    elif piece_type == 'k':
        return get_king_moves(board, x, y, color)
    return []
