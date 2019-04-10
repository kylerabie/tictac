import pygame, sys, os
import numpy as np

from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
SIZE = 300

screen = pygame.display.set_mode((SIZE,SIZE))


def create_board():
    board = np.zeros((3,3))
    return board

board = create_board()
print(board)

def set_piece(board, selx, sely, piece):
    board[selx][sely] = piece

def is_valid(board, selx, sely):
    return board[selx,sely] == 0

def draw_piece(x, y, piece):

    if piece == 1:

        pygame.draw.line(screen, WHITE, [x*100+10, y*100+90], [x*100+90, y*100+10],3)
        pygame.draw.line(screen, WHITE, [x*100+10, y*100+10], [x*100+90, y*100+90],3)

    else:

        pygame.draw.circle(screen, RED, [x*100+50, y*100+50], 40)

def win_move(board, piece):

    if np.sum(np.sum(board == piece, axis=0) == 3) == 1:
        return True

    if np.sum(np.sum(board == piece, axis=1) == 3) == 1:
        return True

    if board[2,0] == piece and board[1,1] == piece and board[0,2] == piece:
        return True

    elif board[0,0] == piece and board[1,1] == piece and board[2,2] == piece:
        return True

turn=0
running = True

screen.fill((0,0,0))
lines = np.linspace(0, SIZE, 4)

for i in lines:

    pygame.draw.line(screen, WHITE, [i, 0], [i, SIZE],3)
    pygame.draw.line(screen, WHITE, [0,i], [SIZE,i],3)

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False



        if event.type == pygame.MOUSEBUTTONDOWN:

            if turn == 0:
                tempx, tempy = pygame.mouse.get_pos()
                col, row = (tempx // 100 , tempy // 100)
                # print(f"player 1 position: {row} and {col}")

                if is_valid(board, row, col):

                    print(f"player 1 position: {row} and {col}")
                    set_piece(board, row, col, 1)
                    draw_piece(col, row, 1)
                    print(board)
                    if win_move(board, 1):
                        print("Congratulations Player 1, you win!")
                        running = False
                else: print("Invalid move, try again!")

            else:

                tempx, tempy = pygame.mouse.get_pos()
                col, row = (tempx // 100 , tempy // 100)
                # print(f"player 2 position: {row} and {col}")

                if is_valid(board, row, col):

                    set_piece(board, row, col, 2)
                    draw_piece(col, row, 2)
                    print(board)
                    if win_move(board, 2):
                        print("Congratulations Player 2, you win!")
                        running = False
                else: print("Invalid move, try again!")

            print(turn)
            turn += 1
            turn = turn % 2

    pygame.display.update()
