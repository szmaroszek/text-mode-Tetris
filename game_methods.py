from random import randint
from os import system, name

# initialise pieces dictionary
pieces = {
    '1': [
        ['****'], 
        ['*', '*', '*', '*'],
        ['****'], 
        ['*', '*', '*', '*'],
        ],
    '2': [
        ['* ', '* ', '**'],
        ['***', '*  '],
        ['**', ' *', ' *'],
        ['  *', '***'],
        ], 
    '3': [
        [' *', ' *', '**'],
        ['*  ', '***'],
        ['**', '* ', '* '],
        ['***', '  *'],
        ],
    '4': [
        [' *', '**', '* '],
        ['** ', ' **'],
        [' *', '**', '* '],
        ['** ', ' **'],
        ], 
    '5': [
        ['**', '**'],
        ['**', '**'],
        ['**', '**'],
        ['**', '**'],
        ]
    }

def printBoard(board):
    for line in board:
        print(line)

def addPiece(board):
    # generate random piece
    piece_type = randint(1, 5)
    piece_rotation = 0
    current_piece = [piece_type, piece_rotation]
    piece = pieces[f'{piece_type}'][piece_rotation]
    # generate random x value to place piece on x-axis 
    x_coordinate = randint(1, 18)
    # if piece goes over the board, generate new random x coordinate
    while x_coordinate + len(piece[0]) > 19 or x_coordinate - len(piece[0]) < 1:
        x_coordinate = randint(1, 18)

    active_coordinates = []
    # add piece to the top of the board
    for y_index, line in enumerate(piece):
        board_line = list(board[y_index])
        board_line[x_coordinate:x_coordinate + len(line)] = line
        board[y_index] = ''.join(board_line)
        # keep track of active piece position
        for x_index, point in enumerate(board_line[1:19]):
            if point == '*':
                active_coordinates.append([x_index +1, y_index])

    return board, active_coordinates, piece, current_piece

def pieceDown(board, active_coordinates, piece, current_piece):
    new_coordinates = []
    # check if the move is valid
    if possibleMove(board, active_coordinates, 'down'):
        # delete active piece
        board = pieceDelete(board, active_coordinates)
        # create active piece 1 row lower
        for point in active_coordinates:
            board_line = list(board[point[1] + 1])
            board_line[point[0]] = '*'
            board[point[1] + 1] = ''.join(board_line)
            new_coordinates.append([point[0], point[1] + 1])
        # check if the next move is valid and if not create new piece
        if not possibleMove(board, new_coordinates, 'down'):
            board, active_coordinates, piece, current_piece = addPiece(board)
            return board, active_coordinates, piece, current_piece

        return board, new_coordinates, piece, current_piece
        
    else:
        for point in active_coordinates:
            new_coordinates.append([point[0], point[1] + 1])
        for point in new_coordinates:
            # check if piece has any valid moves and if not restart the game
            if point[1] == 1:
                board = ['*                  *'] *19 + ['********************']
                board, active_coordinates, piece, current_piece = addPiece(board)
        return board, active_coordinates, piece, current_piece

def pieceLeft(board, active_coordinates):
    new_coordinates = []
    # delete active piece
    board = pieceDelete(board, active_coordinates)

    # create active piece in the next column
    for point in active_coordinates:
        board_line = list(board[point[1]])
        board_line[point[0] - 1] = '*'
        board[point[1]] = ''.join(board_line)
        new_coordinates.append([point[0] - 1, point[1]])

    return board, new_coordinates

def pieceRight(board, active_coordinates):
    new_coordinates = []
    # delete active piece
    board = pieceDelete(board, active_coordinates)

    # create active piece in the next column
    for point in active_coordinates:
        board_line = list(board[point[1]])
        board_line[point[0] + 1] = '*'
        board[point[1]] = ''.join(board_line)
        new_coordinates.append([point[0] + 1, point[1]])

    return board, new_coordinates

def pieceRotate(board, active_coordinates, piece):
    new_coordinates = []
    # delete active piece
    board = pieceDelete(board, active_coordinates)
    active_x, active_y = active_coordinates[0][0], active_coordinates[0][1]

    for y_index, line in enumerate(piece):
        board_line = list(board[active_y + y_index])
        board_line[active_x:active_x + len(line)] = line
        board[active_y + y_index] = ''.join(board_line)

        # keep track of active piece position
        for x_index, point in enumerate(board_line[active_x:active_x + len(line)]):
            if point == '*':
                new_coordinates.append([active_x + x_index, active_y + y_index])

    return board, new_coordinates, piece

def pieceDelete(board, active_coordinates):
    for point in active_coordinates:
        board_line = list(board[point[1]])
        board_line[point[0]] = ' '
        board[point[1]] = ''.join(board_line)
        
    return board

def boardUpdate(board, active_coordinates):
    current_board = []
    for y_index, line in enumerate(board):
        for x_index, point in enumerate(line):
            if point == '*' and [x_index, y_index] not in active_coordinates:
                current_board.append([x_index, y_index])
    return current_board

def possibleMove(board, active_coordinates, move, piece = None):
    # check if particular move is valid
    current_board = boardUpdate(board, active_coordinates)
    if move == 'left':
        for point in active_coordinates:
            if [point[0] - 1, point[1]] in (current_board):
                return False
        return True

    if move == 'right':
        for point in active_coordinates:
            if [point[0] + 1, point[1]] in (current_board):
                return False
        return True

    if move == 'down':
        for point in active_coordinates:
            if [point[0], point[1] + 1] in (current_board):
                return False
        return True
        
    if move == 'rotate' and piece != None:
        active_x, active_y = active_coordinates[0][0], active_coordinates[0][1]
        future_coordinates = []
        for y_index, line in enumerate(piece):
            for x in range(active_x, active_x + len(line)):
                future_coordinates.append([x, active_y + y_index])
        for point in future_coordinates:
            if [point[0], point[1]] in (current_board):
                return False
        return True

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')