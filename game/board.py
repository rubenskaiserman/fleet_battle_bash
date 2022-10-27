from point import Point

class Board:
    name: str
    board_width = 10
    board_height = 10
    board = list
    ships_to_position = []

    def __init__(self, name):
        self.name = name
        self.board = []
        self.ships_to_position= [1, 2, 3, 4, 5, 6]
        for i in range(self.board_width):
            self.board.append([])
            for j in range(self.board_height):
                self.board[i].append('_')

    def print_board(self):
        for line in self.board:
            print(line)

    def can_position(self, start_point:Point, end_point:Point):
        FIRST_INDEX = 0
        LAST_INDEX = 9
        if start_point.x < FIRST_INDEX or start_point.x > LAST_INDEX or start_point.y < FIRST_INDEX or start_point.y > LAST_INDEX:
            return False
        elif end_point.y != start_point.y:
            if abs((end_point.y) - start_point.y) + 1 not in self.ships_to_position:
                return False
            if start_point.x != end_point.x:
                return False
            for point_y in range(start_point.y, end_point.y + 1):
                if self.board[start_point.x][point_y] == 'O':
                    return False
        else:
            if (end_point.x + 1) - start_point.x not in self.ships_to_position:
                return False
            if start_point.y != end_point.y:
                return False
            for point_x in range(start_point.x, end_point.x + 1):
                if self.board[point_x][start_point.y] == 'O':
                    return False
        return True

    def position_ship(self, start_point:Point, end_point:Point):
        if end_point.y > start_point.y:
            for point_y in range(start_point.y, end_point.y + 1):
                self.board[start_point.x][point_y] = 'O'
        else:
            for point_x in range(start_point.x, end_point.x + 1):
                self.board[point_x][start_point.y] = 'O'

    def position_fleet(self):
        for i in range(6):
            while True:
                try:
                    self.print_board()
                    answer = input('Insira a posição de ambas as pontas de seu navio: ').split()
                    start_ship = Point(int(answer[0]), int(answer[1]))
                    end_ship = Point(int(answer[2]), int(answer[3]))
                    if self.can_position(start_ship, end_ship):
                        self.position_ship(start_ship, end_ship)
                        break
                    else:
                        print("A posição desejada não pode ser utilizada. Por favor tente novamente", end="\n\n")
                except:
                    print("Ocorreu um erro, tente novamente", end="\n\n")
