import time

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.', '.', '.'],
                              ['.', '.', '.'],
                              ['.', '.', '.']]
        self.player_turn = 'X'  # Player X always plays first

    def draw_board(self):
        for row in self.current_state:
            print(' | '.join(row))
            print('-' * 9)
        print()

    def is_valid(self, px, py):
        return 0 <= px < 3 and 0 <= py < 3 and self.current_state[px][py] == '.'

    def is_end(self):
        # Check vertical, horizontal and diagonal wins
        for i in range(3):
            if self.current_state[i][0] == self.current_state[i][1] == self.current_state[i][2] != '.':
                return self.current_state[i][0]
            if self.current_state[0][i] == self.current_state[1][i] == self.current_state[2][i] != '.':
                return self.current_state[0][i]

        if self.current_state[0][0] == self.current_state[1][1] == self.current_state[2][2] != '.':
            return self.current_state[0][0]
        if self.current_state[0][2] == self.current_state[1][1] == self.current_state[2][0] != '.':
            return self.current_state[0][2]

        # Check for a tie
        if all(cell != '.' for row in self.current_state for cell in row):
            return '.'

        return None

    def max_alpha_beta(self, alpha, beta):
        maxv = -2
        px, py = None, None
        result = self.is_end()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '.':
            return 0, 0, 0

        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    m, _, _ = self.min_alpha_beta(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px, py = i, j
                    self.current_state[i][j] = '.'
                    if maxv >= beta:
                        return maxv, px, py
                    if maxv > alpha:
                        alpha = maxv

        return maxv, px, py

    def min_alpha_beta(self, alpha, beta):
        minv = 2
        qx, qy = None, None
        result = self.is_end()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '.':
            return 0, 0, 0

        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    m, _, _ = self.max_alpha_beta(alpha, beta)
                    if m < minv:
                        minv = m
                        qx, qy = i, j
                    self.current_state[i][j] = '.'
                    if minv <= alpha:
                        return minv, qx, qy
                    if minv < beta:
                        beta = minv

        return minv, qx, qy

    def play_alpha_beta(self):
        while True:
            self.draw_board()
            result = self.is_end()

            if result is not None:
                if result == 'X':
                    print('The winner is X!')
                elif result == 'O':
                    print('The winner is O!')
                elif result == '.':
                    print("It's a tie!")
                self.initialize_game()
                continue

            if self.player_turn == 'X':
                while True:
                    px = int(input('Insert the X coordinate (0-2): '))
                    py = int(input('Insert the Y coordinate (0-2): '))
                    
                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')
            else:
                start = time.time()
                _, px, py = self.max_alpha_beta(-2, 2)
                end = time.time()
                print('AI plays: X = {}, Y = {}'.format(px, py))
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'


def main():
    g = Game()
    g.play_alpha_beta()

if __name__ == "__main__":
    main()
