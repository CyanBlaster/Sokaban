import sys
import pygame
import datetime
import math
import pygame.freetype

pygame.init()


def ZeroField(n):
    return [[0] * n for i in range(n)]


def createVerticalLine(board, x, y, length):
    if(length < 10):
        for i in range(length):
            board[x][y + i] = 3

def checkWin(holes, board):
    for y in range(10):
            for x in range(10):
                if(holes[x][y] == 2):
                    if(board[x][y] != 1):
                        return False
    return True

def main():
    grass = pygame.image.load('grass1.png')
    cellWidth = 16
    cellHeight = 16
    width = 501
    height = 501
    screen = pygame.display.set_mode((width, height))
    running = True
    xIdx = 2
    yIdx = 2
    playmode = False
    board = ZeroField(10)
    holes = ZeroField(10)
    select = False
    while running:
        if(playmode):
            if(checkWin(holes, board)):
                running = False

        pygame.display.flip()
        screen.fill((0, 0, 0))
        # for i in range(0, 10):
        #     pygame.draw.line(screen, (0, 0, 255), (i * cellWidth, 0), (i * cellHeight, 500))
        #     pygame.draw.line(screen, (0, 0, 255), (0, i * cellWidth), (500, i * cellHeight))
        
        for y in range(10):
            for x in range(10):
                if(board[x][y] == 3):
                    pygame.draw.rect(screen, (139, 69, 19), (x * cellWidth + 1, y * cellHeight + 1, cellWidth - 1, cellHeight - 1))
                if(holes[x][y] == 2):
                    pygame.draw.rect(screen, (0, 255, 0), (x * cellWidth + 1, y * cellHeight + 1, cellWidth - 1, cellHeight - 1))
                if(board[x][y] == 1):
                    pygame.draw.rect(screen, (0, 0, 255), (x * cellWidth + 1, y * cellHeight + 1, cellWidth - 1, cellHeight - 1))
                if(board[x][y] == 0):
                    screen.blit(grass, (x * cellWidth + 1, y * cellHeight + 1))
        
        if(playmode == False):
            pygame.draw.rect(screen, (255, 255, 255), (xIdx * cellWidth + 1, yIdx * cellHeight + 1, cellWidth - 1, cellHeight - 1), 1, border_radius=1)
        else:
            pygame.draw.rect(screen, (255, 255, 255), (xIdx * cellWidth + 1, yIdx * cellHeight + 1, cellWidth - 1, cellHeight - 1))
            
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    if(playmode):
                        if(board[xIdx - 1][yIdx] != 3):
                            if(xIdx > 1 and board[xIdx - 1][yIdx] == 1 and board[xIdx - 2][yIdx] != 3 and board[xIdx - 2][yIdx] != 1):
                                board[xIdx - 2][yIdx] = 1
                                board[xIdx - 1][yIdx] = 0
                            if(xIdx > 0 and board[xIdx - 1][yIdx] != 1):
                                xIdx -= 1
                            if(xIdx == -1):
                                xIdx = 0
                    else:
                        xIdx -= 1
                        if(xIdx == -1):
                            xIdx = 0
                elif events.key == pygame.K_RIGHT:
                    if(playmode):
                        if(board[xIdx + 1][yIdx] != 3):
                            if(xIdx < 8 and board[xIdx + 1][yIdx] == 1 and board[xIdx + 2][yIdx] != 3 and board[xIdx + 2][yIdx] != 1):
                                board[xIdx + 2][yIdx] = 1
                                board[xIdx + 1][yIdx] = 0
                            if(xIdx < 9 and board[xIdx + 1][yIdx] != 1):
                                xIdx += 1
                            if(xIdx == 10):
                                xIdx = 9
                    else:
                        xIdx += 1
                        if(xIdx == 10):
                            xIdx = 9
                elif events.key == pygame.K_UP:
                    if(playmode):
                        if(board[xIdx][yIdx - 1] != 3):
                            if(yIdx > 1 and board[xIdx][yIdx - 1] == 1 and board[xIdx][yIdx - 2] != 3 and board[xIdx][yIdx - 2] != 1):
                                board[xIdx][yIdx - 2] = 1
                                board[xIdx][yIdx - 1] = 0
                            if(yIdx > 0 and board[xIdx][yIdx - 1] != 1):
                                yIdx -= 1
                            if(yIdx == -1):
                                yIdx = 0
                    else:
                        yIdx -= 1
                        if(yIdx == -1):
                            yIdx = 0
                elif events.key == pygame.K_DOWN:
                    if(playmode):
                        if(board[xIdx][yIdx + 1] != 3):
                            if(yIdx < 8 and board[xIdx][yIdx + 1] == 1 and board[xIdx][yIdx + 2] != 3 and board[xIdx][yIdx + 2] != 1):
                                board[xIdx][yIdx + 2] = 1
                                board[xIdx][yIdx + 1] = 0
                            if(yIdx < 9 and board[xIdx][yIdx + 1] != 1):
                                yIdx += 1
                            if(yIdx == 10):
                                yIdx = 9
                            
                    else:
                        yIdx += 1
                        if(yIdx == 10):
                            yIdx = 9
                elif events.key == pygame.K_d:
                    if(playmode == False):
                        holes[xIdx][yIdx] = 2
                elif events.key == pygame.K_f:
                    if(playmode == False):
                        board[xIdx][yIdx] = 1
                elif events.key == pygame.K_s:
                     if(playmode == False):
                        board[xIdx][yIdx] = 3
                elif events.key == pygame.K_a:
                             if(playmode == False):
                                if(board[xIdx][yIdx] != 0):
                                    pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellWidth + 1, yIdx * cellHeight + 1, cellWidth - 1, cellHeight - 1))
                                    board[xIdx][yIdx] = 0
                                elif(holes[xIdx][yIdx] != 0):
                                    pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellWidth + 1, yIdx * cellHeight + 1, cellWidth - 1, cellHeight - 1))
                                    holes[xIdx][yIdx] = 0
                elif events.key == pygame.K_p:
                    if(playmode):
                        playmode = False
                        select = False
                    else:
                        playmode = True
                
                elif events.key == pygame.K_SPACE:
                    if(playmode):
                        if(select == True):
                            select = False
                            for y in range(10):
                               for x in range(10):
                                   if(board[x][y] == 1):
                                      pygame.draw.rect(screen, (0, 0, 0), (x * cellWidth + 1, y * cellHeight + 1, cellWidth - 1, cellHeight - 1))
                                      board[x][y] = 0
                            board[xIdx][yIdx] = 1
                        else:
                            if(board[xIdx][yIdx] == 1):
                               select = True
                        
main()