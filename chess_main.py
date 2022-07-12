class Piece():
    '''
    def __init__(self) -> None:
        pass
    '''
    def __init__(self, role = 0, color = 0):
        self.role = role
        self.color = color
        self.new = True # for pawn double movement and castling
        self.deads = []

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

class Board():
    def __init__(self):                             # LOOK UP K/Q PLACEMENT
        temp = [Piece(2, 1), Piece(3, 1), Piece(4, 1), Piece(6, 1),
        Piece(5, 1), Piece(4, 1), Piece(3, 1), Piece(2, 1)]     #  black special pieces
        temp2 = [Piece(1, 1) for x in range(8)]                 #  black pawns
        temp3 = [Piece() for x in range(8)]
        temp4 = [Piece() for x in range(8)]
        temp5 = [Piece() for x in range(8)]
        temp6 = [Piece() for x in range(8)]
        temp7 = [Piece(1, 2) for x in range(8)]
        temp8 = [Piece(2, 2), Piece(3, 2), Piece(4, 2), Piece(6, 2),
        Piece(5, 2), Piece(4, 2), Piece(3, 2), Piece(2, 2)]
        self.pieces = [temp, temp2, temp3, temp4, temp5, temp6, temp7, temp8]
        self.win = 0
    def printBoard(self):
        print("Printing board...")
        for i in range(8):
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
                print(' ', end = '')
            print('\n')
    def getSpace(self, space):
        temp = [-1, -1]
        if len(space) == 2 and space[0] in cols.keys() and space[1] in rows.keys():
            temp = [rows[space[1]], cols[space[0]]]
        return temp
    def getPossibleSpaces(self, row, col):
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
        elif piece.role == 2 or piece.role == 5:               # this won't depend on different colors #to fix later cuz picky - change if else format to same as bishop
            for i in range(row - 1, -1, -1):
                if self.pieces[i][col].color == 0:
                    maybeSpaces.append([i, col])
                elif self.pieces[i][col].color != piece.color:
                    maybeSpaces.append([i, col])
                    break
                else:
                    break
            for i in range(row + 1, 8, 1):
                if self.pieces[i][col].color == 0:
                    maybeSpaces.append([i, col])
                elif self.pieces[i][col].color != piece.color:
                    maybeSpaces.append([i, col])
                    break
                else:
                    break
            for i in range(col - 1, -1, -1):
                if self.pieces[row][i].color == 0:
                    maybeSpaces.append([row, i])
                elif self.pieces[row][i].color != piece.color:
                    maybeSpaces.append([row, i])
                    break
                else:
                    break
            for i in range(col + 1, 8, 1):
                if self.pieces[row][i].color == 0:
                    maybeSpaces.append([row, i])
                elif self.pieces[row][i].color != piece.color:
                    maybeSpaces.append([row, i])
                    break
                else:
                    break
        elif piece.role == 3:               # this won't depend on different colors
            knightSpaces = [[row - 2, col - 1], [row - 2, col + 1], [row - 1, col - 2], [row - 1, col + 2],
            [row + 1, col - 2], [row + 1, col + 2], [row + 2, col - 1], [row + 2, col + 1]]
            for i in knightSpaces:
                if i[0] > -1 and i[0] < 8 and i[1] > -1 and i[1] < 8 and self.pieces[i[0]][i[1]].color != piece.color:
                    maybeSpaces.append(i)
        elif piece.role == 4 or piece.role == 5:
            movements = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
            for j in movements:
                for i in range(1, 8):
                    if row + i * j[0] > -1 and row + i * j[0] < 8 and col + i * j[1] > -1 and col + i * j[1] < 8 and self.pieces[row + i * j[0]][col + i * j[1]].color != piece.color:
                        maybeSpaces.append([row + i * j[0], col + i * j[1]])
                        if self.pieces[row + i * j[0]][col + i * j[1]].color != 0:
                            break
                    else:
                        break
        elif piece.role == 7:
            movements = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            for i in movements:
                if row + i[0] > -1 and row + i[0] < 8 and col + i[1] > -1 and col + i[1] < 8 and self.pieces[i[0]][i[1]].color != piece.color:
                    maybeSpaces.append([i[0], i[1]])
        return maybeSpaces


    def move(self, color):
        space = input("Select a piece to move: ")
        coords = self.getSpace(space)
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
                        if self.pieces[destCoords[0]][destCoords[1]].role == 6:
                            self.win = color        
                        self.pieces[destCoords[0]][destCoords[1]] = self.pieces[coords[0]][coords[1]]
                        self.pieces[coords[0]][coords[1]] = Piece()
                        break
                    else:
                        space = input("You cannot place your piece there. Select a piece to move: ")
                        coords = self.getSpace(space)


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
    winner = 1 if test.win == 2 else 2
    
    print("!!!GAME OVER!!!")
    print(f"Player {winner} has won! Congrats!")

if __name__ == "__main__":
    main()