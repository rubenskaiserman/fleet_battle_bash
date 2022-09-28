class Point:
    x: int
    y: int
    def __init__(self, x:int, y:int):
       # TODO Finalizar classe point

class Board:
    name: str
    board_width = 10
    board_height = 10
    board = []

    def __init__(self, name):
        self.name = name
        for i in range(self.board_width):
            self.board.append([])
            for j in range(self.board_height):
                self.board[i].append('_')

    def print_board(self):
        for line in self.board:
            print(line)

    def position_fleet():
        smallest_ship = 1
        biggest_ship = 6
        for i in range(smallest_ship, biggest_ship + 1):
            answer = input('Insira a posição de ambas as pontas de seu navio: ')
            # TODO Finalizar método de posicionamento de navios



def show_introduction():
    with open('intro.txt') as file:
        intro = file.read()
        print(intro)


def main():
    show_introduction()
    input('Press Enter to Start...')
    player1 = Board(input('Insira o nome do jogador 1'))
    player1.position_fleet()
    
    

if __name__=='__main__':
    main()