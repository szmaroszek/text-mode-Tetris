from game_methods import *
from time import sleep

# initialise the board
board = ['*                  *'] *19 + ['********************']

top = False
board, active_coordinates, piece, current_piece = addPiece(board)

# start the game
while not top:
    clear()
    printBoard(board)

    # get user input
    move_input = True
    while move_input:

        print('a - Move Left')
        print('d - Move Right')
        print('w - Rotate Left')
        print('s - Rotate Right')
        user_input = input('Make a move!:')

        if user_input == 'a':
            # check if left is a viable move
            if possibleMove(board, active_coordinates, 'left'):
                board, active_coordinates = pieceLeft(board, active_coordinates)
                board, active_coordinates, piece, current_piece = pieceDown(board, active_coordinates, piece, current_piece)
                board, active_coordinates, piece, current_piece = checkBottom(board, active_coordinates, piece, current_piece)
                board, active_coordinates, piece, current_piece = checkTop(board, active_coordinates, piece, current_piece)
            else:
                clear()
                printBoard(board)
                print('Invalid move!')
                sleep(1)
            move_input = False

        elif user_input == 'd':
            # check if right is a viable move
            if possibleMove(board, active_coordinates, 'right'):
                board, active_coordinates = pieceRight(board, active_coordinates)
                board, active_coordinates, piece, current_piece = pieceDown(board, active_coordinates, piece, current_piece)
                board, active_coordinates, piece, current_piece = checkBottom(board, active_coordinates, piece, current_piece)
                board, active_coordinates, piece, current_piece = checkTop(board, active_coordinates, piece, current_piece)
            else:
                clear()
                printBoard(board)
                print('Invalid move!')
                sleep(1)
            move_input = False

        elif user_input == 'w':
            # initialise next piece orientation
            if current_piece[1] == 0:
                current_piece[1] = 3
            else:
                current_piece[1] -= 1
            # check if rotate is a viable move
            if possibleMove(board, active_coordinates, 'rotate', pieces[f'{current_piece[0]}'][current_piece[1]]):
                board, active_coordinates, piece = pieceRotate(board, active_coordinates, pieces[f'{current_piece[0]}'][current_piece[1]])
                board, active_coordinates, piece, current_piece = pieceDown(board, active_coordinates, piece, current_piece)
                board, active_coordinates, piece, current_piece = checkBottom(board, active_coordinates, piece, current_piece)
                board, active_coordinates, piece, current_piece = checkTop(board, active_coordinates, piece, current_piece)
            else:
                clear()
                printBoard(board)
                print('Invalid move!')
                sleep(1)
            move_input = False

        elif user_input == 's':
            # initialise the next piece orientation
            if current_piece[1] == 3:
                current_piece[1] = 0
            else:
                current_piece[1] += 1
            # check if rotate is a viable move
            if possibleMove(board, active_coordinates, 'rotate', pieces[f'{current_piece[0]}'][current_piece[1]]):
                board, active_coordinates, piece = pieceRotate(board, active_coordinates, pieces[f'{current_piece[0]}'][current_piece[1]])
                board, active_coordinates, piece, current_piece = pieceDown(board, active_coordinates, piece, current_piece)
                board, active_coordinates, piece, current_piece = checkBottom(board, active_coordinates, piece, current_piece)
                board, active_coordinates, piece, current_piece = checkTop(board, active_coordinates, piece, current_piece)
            else:
                clear()
                printBoard(board)
                print('Invalid move!')
                sleep(1)
            move_input = False
        # catch invalid input
        else:
            clear()
            printBoard(board)
            print('Invalid command!')
            sleep(1)
            move_input = False 