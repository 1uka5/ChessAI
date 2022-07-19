'''
TODO: Probably need to split up class declarations and main into separate files
TODO: Implement castling
TODO: Implement en passant
'''
from platform import java_ver
import pygame

from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
 
pygame.init()
X = 400
Y = 400
display_surface = pygame.display.set_mode((X, Y))
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Square:
    def __init__(self, x_start, y_start, width_height, color):
        self.x_start = x_start
        self.y_start = y_start
        self.width_height = width_height
        self.color = color
        self.image = 0

class PieceImage:
    def __init__(self, x_start, y_start, width_height):
        self.x_start = x_start
        self.y_start = y_start
        self.width_height = width_height
        self.image = 0
        self.piece = 0
        self.color = -1

    def draw(self, x, y, piece, color):
        self.color = color
        if piece == 1:
            if color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whitepawn.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackpawn.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
        if piece == 2:
            if color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whiterook.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackrook.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
        if piece == 3:
            if color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whitehorse.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackhorse.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
        if piece == 4:
            if color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whitebishop.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackbishop.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
        if piece == 5:
            if color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whitequeen.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackqueen.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
        if piece == 6:
            if color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whiteking.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackking.png")
                self.image = pygame.transform.scale(self.image, (self.width_height - 5, self.width_height))  
        if self.image != 0:
            screen.blit(self.image, (x, y))
        self.piece = piece

    def erase(self, color):
        surf = pygame.Surface((self.width_height, self.width_height))
        print(self.width_height)
        if color == 0:
            print("a")
            surf.fill((118, 150, 86))
            rect = surf.get_rect()
            screen.blit(surf, (self.x_start, self.y_start))
            pygame.display.flip()
        else:
            print("b")
            surf.fill((255,255,255))
            rect = surf.get_rect()
            screen.blit(surf, (self.x_start, self.y_start))
            pygame.display.flip()
        self.piece = 0

        return color


class Piece():
    def __init__(self, role = 0, color = 0): 
        self.role = role
        self.color = color
        self.new = True # for pawn double movement and castling
        self.age = 0 # for en passant
        self.image = 0
        if self.role == 1:
            if self.color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whitepawn.png")
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackpawn.png")
        if self.role == 2:
            if self.color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whiterook.png")
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackrook.png")
        if self.role == 3:
            if self.color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whitehorse.png")
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackhorse.png")
        if self.role == 4:
            if self.color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whitebishop.png")
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackbishop.png")
        if self.role == 5:
            if self.color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whitequeen.png")
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackqueen.png")
        if self.role == 6:
            if self.color == 0:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/whiteking.png")
            else:
                self.image = pygame.image.load("C:/Users/justi/code/ChessAI/assets/blackking.png")

'''
ROLES:
0: empty
1: pawn
2: rook
3: knight
4: bishop
5: queen
6: king

COLORS:
0: none
1: black
2: white
'''

cols = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
rows = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}
upgrades = {'P': 1, 'R': 2, 'N': 3, 'B': 4, 'Q': 5}

class Board():
    def __init__(self):                             # LOOK UP K/Q PLACEMENT
        temp = [Piece(2, 1), Piece(3, 1), Piece(4, 1), Piece(5, 1),
        Piece(6, 1), Piece(4, 1), Piece(3, 1), Piece(2, 1)]     #  black special pieces
        temp2 = [Piece(1, 1) for x in range(8)]                 #  black pawns
        temp3 = [Piece() for x in range(8)]
        temp4 = [Piece() for x in range(8)]
        temp5 = [Piece() for x in range(8)]
        temp6 = [Piece() for x in range(8)]
        temp7 = [Piece(1, 2) for x in range(8)]
        temp8 = [Piece(2, 2), Piece(3, 2), Piece(4, 2), Piece(5, 2),
        Piece(6, 2), Piece(4, 2), Piece(3, 2), Piece(2, 2)]
        self.pieces = [temp, temp2, temp3, temp4, temp5, temp6, temp7, temp8]
        self.win = 0
    def printBoard(self):
        print("Printing board...")
        for i in range(8):
            print(f"{8-i}   ", end = "")
            for j in range(8):
                piece = self.pieces[i][j]
                if piece.color == 1:
                    if piece.role == 1:
                        print('p', end = '')
                    if piece.role == 2:
                        print('r', end = '')
                    if piece.role == 3:
                        print('n', end = '')
                    if piece.role == 4:
                        print('b', end = '')
                    if piece.role == 5:
                        print('q', end = '')
                    if piece.role == 6:
                        print('k', end = '')
                elif piece.color == 2:
                    if piece.role == 1:
                        print('P', end = '')
                    if piece.role == 2:
                        print('R', end = '')
                    if piece.role == 3:
                        print('N', end = '')
                    if piece.role == 4:
                        print('B', end = '')
                    if piece.role == 5:
                        print('Q', end = '')
                    if piece.role == 6:
                        print('K', end = '')
                else:
                    print('X', end = '')
                print("  ", end = '')
            print('\n')
        print("    A  B  C  D  E  F  G  H")
    def getSpace(self, space):
        temp = [-1, -1]
        if len(space) == 2 and space[0] in cols.keys() and space[1] in rows.keys():
            temp = [rows[space[1]], cols[space[0]]]
        return temp
    def getPossibleSpaces(self, row, col):       # returns a list of possible spaces for a piece, not taking check into account
        piece = self.pieces[row][col]
        maybeSpaces = []
        if piece.role == 1:
            if piece.color == 1 and row < 7:
                if self.pieces[row + 1][col].color == 0:
                    maybeSpaces.append([row + 1, col])
                    if row == 1 and self.pieces[row + 2][col].color == 0:
                        maybeSpaces.append([row + 2, col])
                if col > 0 and self.pieces[row + 1][col - 1].color == 2:
                    maybeSpaces.append([row + 1, col - 1])
                if col < 7 and self.pieces[row + 1][col + 1].color == 2:
                    maybeSpaces.append([row + 1, col + 1])
            elif piece.color == 2 and row > 0:
                if self.pieces[row - 1][col].color == 0:
                    maybeSpaces.append([row - 1, col])
                    if row == 6 and self.pieces[row - 2][col].color == 0:
                        maybeSpaces.append([row - 2, col])
                if col > 0 and self.pieces[row - 1][col - 1].color == 1:
                    maybeSpaces.append([row - 1, col - 1])
                if col < 7 and self.pieces[row - 1][col + 1].color == 1:
                    maybeSpaces.append([row - 1, col + 1])
        if piece.role == 2 or piece.role == 5:               # this won't depend on different colors
            movements = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for j in movements:
                for i in range(1, 8):
                    if row + i * j[0] > -1 and row + i * j[0] < 8 and col + i * j[1] > -1 and col + i * j[1] < 8 and self.pieces[row + i * j[0]][col + i * j[1]].color != piece.color:
                        maybeSpaces.append([row + i * j[0], col + i * j[1]])
                        if self.pieces[row + i * j[0]][col + i * j[1]].color != 0:
                            break
                    else:
                        break
        if piece.role == 3:               # this won't depend on different colors
            knightSpaces = [[row - 2, col - 1], [row - 2, col + 1], [row - 1, col - 2], [row - 1, col + 2],
            [row + 1, col - 2], [row + 1, col + 2], [row + 2, col - 1], [row + 2, col + 1]]
            for i in knightSpaces:
                if i[0] > -1 and i[0] < 8 and i[1] > -1 and i[1] < 8 and self.pieces[i[0]][i[1]].color != piece.color:
                    maybeSpaces.append(i)
        if piece.role == 4 or piece.role == 5:
            movements = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
            for j in movements:
                for i in range(1, 8):
                    if row + i * j[0] > -1 and row + i * j[0] < 8 and col + i * j[1] > -1 and col + i * j[1] < 8 and self.pieces[row + i * j[0]][col + i * j[1]].color != piece.color:
                        maybeSpaces.append([row + i * j[0], col + i * j[1]])
                        if self.pieces[row + i * j[0]][col + i * j[1]].color != 0:
                            break
                    else:
                        break
        if piece.role == 6:
            movements = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            for i in movements:
                if row + i[0] > -1 and row + i[0] < 8 and col + i[1] > -1 and col + i[1] < 8 and self.pieces[row + i[0]][col + i[1]].color != piece.color:
                    maybeSpaces.append([row + i[0], col + i[1]])
        return maybeSpaces
    def inCheck(self, color):
        kingCoords = [-1, -1]
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j].color == color and self.pieces[i][j].role == 6:
                    kingCoords = [i, j]
                    break
            if kingCoords[0] != -1:
                break
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j].color != color and kingCoords in self.getPossibleSpaces(i, j):
                    return True
        return False
    def checkStalemate(self, color):
        opp = 2 if color == 1 else 1
        mate = True
        check = self.inCheck(opp)
        temp = []
        for i in range(8):
            temptemp = []
            for j in range(8):
                temptemptemp = self.pieces[i][j]
                temptemp.append(temptemptemp)
            temp.append(temptemp)
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j].color == opp:
                    for k in self.getPossibleSpaces(i, j):
                        piece1 = self.pieces[i][j]
                        piece2 = self.pieces[k[0]][k[1]]
                        self.pieces[k[0]][k[1]] = piece1
                        self.pieces[i][j] = Piece()
                        if not self.inCheck(opp):
                            mate = False
                            self.pieces[i][j] = piece1
                            self.pieces[k[0]][k[1]] = piece2
                            break
                        else:
                            self.pieces[i][j] = piece1
                            self.pieces[k[0]][k[1]] = piece2
                if not mate:
                    break
            if not mate:
                break
        self.pieces = temp
        if mate:
            if check:
                self.win = color
                print("Checkmate!")
            else:
                self.win = 3
                print("Stalemate!")
    def move(self, color):
        space = input("Select a piece to move: ")
        coords = self.getSpace(space)
        '''
        Code to see if all moves result with player in check
        '''
        while True:
            if coords[0] == -1:
                space = input("Input not understood (check for capitalization or whitespace). Select a piece to move: ")
                coords = self.getSpace(space)
            elif self.pieces[coords[0]][coords[1]].color != color:
                space = input("You do not have a piece at that space. Select a piece to move: ")
                coords = self.getSpace(space)
            else:
                space = input("Select a space to move your piece to: ")             # remember to deal with king in check
                destCoords = self.getSpace(space)
                if destCoords[0] == -1:
                    space = input("Input not understood (check for capitalization or whitespace). Select a piece to move: ")
                    coords = self.getSpace(space)
                else:
                    if destCoords in self.getPossibleSpaces(coords[0], coords[1]):   
                        temp = self.pieces
                        self.pieces[destCoords[0]][destCoords[1]] = self.pieces[coords[0]][coords[1]]
                        self.pieces[coords[0]][coords[1]] = Piece()
                        if self.inCheck(color):
                            self.pieces = temp
                            print("You cannot move there, because you are putting yourself in check. Select a piece to move: ")
                            coords = self.getSpace(space)
                        else:
                            if temp[destCoords[0]][destCoords[1]].color != 0:
                                print("You have captured a piece!")
                            if self.pieces[destCoords[0]][destCoords[1]].role == 1 and ((color == 1 and destCoords[0] == 7) or (color == 2 and destCoords[0] == 0)):
                                print("You can upgrade your pawn!")
                                space = input("What would you like to upgrade your pawn to (P, R, N, B, Q)? ")
                                while not space in upgrades.keys():
                                    space = print("Input not understood (check for capitalization or whitespace). What would you like to upgrade your pawn to? (P, R, N, B, Q)")
                                self.pieces[destCoords[0]][destCoords[1]].role = upgrades[space]
                            break
                    else:
                        space = input("You cannot place your piece there. Select a piece to move: ")
                        coords = self.getSpace(space)
        self.staleCheckmate(color)


def calculate_coordinates(x_array, y_array, color):
    if SCREEN_WIDTH <= SCREEN_HEIGHT:
        width_height = SCREEN_WIDTH / 8
    else:
        width_height = SCREEN_HEIGHT / 8
    
    x_coordinate = x_array * width_height
    y_coordinate = y_array * width_height

    return Square(x_coordinate, y_coordinate, width_height, color)

def calculate_image_coordinates(x_array, y_array):
    if SCREEN_WIDTH <= SCREEN_HEIGHT:
        width_height = SCREEN_WIDTH / 8
    else:
        width_height = SCREEN_HEIGHT / 8
    
    x_coordinate = x_array * width_height
    y_coordinate = y_array * width_height

    return PieceImage(x_coordinate, y_coordinate, width_height)



def main(): # remember to deal with king in check
    test = Board()

    chess_board = []
    pieces = []
    color = 1 # 1 is black
    for i in range(8):
        chess_row = []
        color = not color
        for j in range(8):
            chess_row.append(calculate_coordinates(i, j, color))
            color = not color
        chess_board.append(chess_row)

    for i in range(8):
        pieces_row = []
        for j in range(8):
            if j == 0:
                color = 1
                if i == 0 or i == 7:
                    pieces_row.append(calculate_image_coordinates(i, j)) 
                elif i == 1 or i == 6:
                    pieces_row.append(calculate_image_coordinates(i, j))
                elif i == 2 or i == 5:
                    pieces_row.append(calculate_image_coordinates(i, j))
                elif i == 3:
                    pieces_row.append(calculate_image_coordinates(i, j))
                elif i == 4:
                    pieces_row.append(calculate_image_coordinates(i, j))
            elif j == 1:
                color = 1
                pieces_row.append(calculate_image_coordinates(i, j))
            elif j == 6:
                color = 0
                pieces_row.append(calculate_image_coordinates(i, j))
            elif j == 7:
                color = 0
                if i == 0 or i == 7:
                    pieces_row.append(calculate_image_coordinates(i, j)) 
                elif i == 1 or i == 6:
                    pieces_row.append(calculate_image_coordinates(i, j))
                elif i == 2 or i == 5:
                    pieces_row.append(calculate_image_coordinates(i, j))
                elif i == 3:
                    pieces_row.append(calculate_image_coordinates(i, j))
                elif i == 4:
                    pieces_row.append(calculate_image_coordinates(i, j))
            else:
                pieces_row.append(calculate_image_coordinates(i, j))
        pieces.append(pieces_row)

    
    for row in chess_board:
        for square in row:
            surf = pygame.Surface((square.width_height, square.width_height))
    
            if square.color == 1:
                surf.fill((255, 255, 255))
            else:
                surf.fill((118, 150, 86))

            #display_surface.blit(square.image, (square.x_start, square.y_start))
    
            rect = surf.get_rect()
            screen.blit(surf, (square.x_start, square.y_start))
            pygame.display.flip()

    def get_square_for_position(pos):
        for row in chess_board:
            if row[0].y_start < pos[1] < row[0].y_start + row[0].width_height:
                for square in row:
                    if square.x_start < pos[0] < square.x_start + square.width_height:
                        return square

    # pieces = []
    # for i in range(8):
    #     for j in range(8):
            
    for i in range(8):
        for j in range(8):
            if j == 0:
                color = 1
                if i == 0 or i == 7:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 2, color) 
                elif i == 1 or i == 6:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 3, color)
                elif i == 2 or i == 5:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 4, color)
                elif i == 3:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 5, color)
                elif i == 4:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 6, color)
            elif j == 1:
                color = 1
                pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 1, color)
            elif j == 6:
                color = 0
                pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 1, color)
            elif j == 7:
                color = 0
                if i == 0 or i == 7:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 2, color)
                elif i == 1 or i == 6:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 3, color)
                elif i == 2 or i == 5:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 4, color)
                elif i == 3:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 5, color)
                elif i == 4:
                    pieces[i][j].draw(pieces[i][j].x_start, pieces[i][j].y_start, 6, color)



    running = True
    piece_clicked = False
    original_pos = [-1, -1]
    prev_piece = -1
    while running:
        for event in pygame.event.get():
            #display_surface.blit(chess_board[0][0].image, (chess_board[0][0].x_start, chess_board[0][0].y_start))
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
    
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                pos = (int(pos[0] // 87.5), int(pos[1] // 87.5))
                print((pos))
                if not piece_clicked and pieces[pos[0]][pos[1]].piece != 0 and pieces[pos[0]][pos[1]].color == 0:
                    piece_clicked = True
                    print("Piece clicked")
                    piece_clicked = pos
                    print(len(pieces))
                    print(len(pieces[0]))
                    original_pos = pos
                    prev_piece = pieces[pos[0]][pos[1]].piece
                    prev_color = pieces[pos[0]][pos[1]].color
                    surf_h = pygame.Surface((pieces[pos[0]][pos[1]].width_height, 5))
                    surf_v = pygame.Surface((5, pieces[pos[0]][pos[1]].width_height))
                    surf_h.fill((255, 0, 0))
                    surf_v.fill((255, 0, 0))
                    rect = surf.get_rect()
                    screen.blit(surf_v, (pieces[pos[0]][pos[1]].x_start, pieces[pos[0]][pos[1]].y_start))
                    screen.blit(surf_v, (pieces[pos[0]][pos[1]].x_start + pieces[pos[0]][pos[1]].width_height - 5, pieces[pos[0]][pos[1]].y_start))
                    screen.blit(surf_h, (pieces[pos[0]][pos[1]].x_start, pieces[pos[0]][pos[1]].y_start + pieces[pos[0]][pos[1]].width_height - 5))
                    screen.blit(surf_h, (pieces[pos[0]][pos[1]].x_start, pieces[pos[0]][pos[1]].y_start))
                    pygame.display.flip()
                elif piece_clicked: 
                    print("Piece moved")
                    piece_clicked = False
                    print(original_pos)
                    print(chess_board[original_pos[0]][original_pos[1]].color)
                    color = pieces[original_pos[0]][original_pos[1]].erase(chess_board[original_pos[0]][original_pos[1]].color)
                    pieces[pos[0]][pos[1]].draw(pieces[pos[0]][pos[1]].x_start, pieces[pos[0]][pos[1]].y_start, prev_piece, prev_color)


            elif event.type == QUIT:
                running = False
                pygame.quit()

            pygame.display.update() 

    while test.win == 0:
        test.printBoard()
        print('Player 1\'s Turn!')
        test.move(2)
        if test.win != 0:
            break
        test.printBoard()
        print('Player 2\'s Turn!')
        test.move(1)
    winner = 1 if test.win == 2 else (2 if test.win == 1 else 0)
    
    if winner != 0:
        print("Player {winner} has won! Congrats!")

if __name__ == "__main__":
    main()