'''
TODO: Probably need to split up class declarations and main into separate files
TODO: Implement castling
TODO: Implement en passant
'''

class Piece():
    def __init__(self, role = 0, color = 0):
        self.role = role
        self.color = color
        self.new = True # for pawn double movement and castling
        self.age = 0 # for en passant

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


def main(): # remember to deal with king in check
    test = Board()

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
        print(f"Player {winner} has won! Congrats!")

if __name__ == "__main__":
    main()