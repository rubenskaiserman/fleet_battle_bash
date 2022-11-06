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
            print("Os vetores inseridos não correspondem a posições possíveis")
            return False
        if end_point.y != start_point.y:
            if abs((end_point.y) - start_point.y) + 1 not in self.ships_to_position:
                print("O tamanho do navio indicado não está disponível")
                return False
            if start_point.x != end_point.x:
                print("O navio selecionado não pode ser posicionado pois não é uma reta")
                return False
            if start_point.y < end_point.y:
                for point_y in range(start_point.y, end_point.y + 1):
                    if self.board[point_y][start_point.x] == 'O':
                        print("A posição selecionada está indisponível")
                        return False
            else:
                for point_y in range(end_point.y, start_point.y + 1):
                    if self.board[point_y][start_point.x] == 'O':
                        print("A posição selecionada está indisponível")
                        return False
        else:
            if (end_point.x + 1) - start_point.x not in self.ships_to_position:
                print("O tamanho do navio indicado não está disponível")
                return False
            if start_point.x < end_point.x:
                for point_x in range(start_point.x, end_point.x + 1):
                    if self.board[start_point.y][point_x] == 'O':
                        print("A posição selecionada está indisponível")
                        return False
            else:
                for point_x in range(end_point.x, start_point.x + 1):
                    if self.board[start_point.y][point_x] == 'O':
                        print("A posição selecionada está indisponível")
                        return False
        return True

    def position_ship(self, start_point:Point, end_point:Point):
        if abs(end_point.y - start_point.y) > 0:
            length = abs(end_point.y - start_point.y) + 1
            if start_point.y < end_point.y:
                for point_y in range(start_point.y, end_point.y + 1):
                    self.board[point_y][start_point.x] = 'O'
            else:
                for point_y in range(end_point.y, start_point.y + 1):
                    self.board[point_y][start_point.x] = 'O'
        else:
            length = abs(end_point.x - start_point.x) + 1
            if start_point.x < end_point.x:
                for point_x in range(start_point.x, end_point.x + 1):
                    self.board[start_point.y][point_x] = 'O'
            else:
                for point_x in range(end_point.x, start_point.x + 1):
                    self.board[start_point.y][point_x] = 'O'
        self.ships_to_position.remove(length)

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
                except:
                    print("Ocorreu um erro, tente novamente", end="\n\n")
