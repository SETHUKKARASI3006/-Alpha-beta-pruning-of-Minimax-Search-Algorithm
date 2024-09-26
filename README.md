<h1>ExpNo 7 : Implement Alpha-beta pruning of Minimax Search Algorithm for a Simple TIC-TAC-TOE game</h1> 
<h3>Name:       </h3>
<h3>Register Number/Staff Id:           </h3>
<H3>Aim:</H3>
<p>
Implement Alpha-beta pruning of Minimax Search Algorithm for a Simple TIC-TAC-TOE game
</p>
<h1>GOALS of Alpha-Beta Pruning in MiniMax Search Algorithm</h1>

<h3>Improve the decision-making efficiency of the computer player by reducing the number of evaluated nodes in the game tree.</h3>
<h3>Tic-Tac-Toe game implementation incorporating the Alpha-Beta pruning and the Minimax algorithm with Python Code.</h3>
<h1>IMPLEMENTATION</h1>

The project involves developing a Tic-Tac-Toe game implementation incorporating the Alpha-Beta pruning with the Minimax algorithm. Using this algorithm, the computer player analyzes the game state, evaluates possible moves, and selects the optimal action based on the anticipated outcomes.

<h1>The Minimax algorithm</h1>

recursively evaluates all possible moves and their potential outcomes, creating a game tree.

<h1>Alpha-Beta pruning</h1>

Alpha–Beta (𝛼−𝛽) algorithm is actually an improved minimax using a heuristic. It stops evaluating a move when it makes sure that it’s worse than a previously examined move. Such moves need not to be evaluated further.

When added to a simple minimax algorithm, it gives the same output but cuts off certain branches that can’t possibly affect the final decision — dramatically improving the performance


<hr>
<h2>Program:</h2>
<hr>

```
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
```


<hr>
<h2>Sample Input and Output:</h2>

![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/8d5e329a-9aff-41a6-bcf0-46efa10e1b92)
![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/438b242d-54ba-443e-b040-a936e6ae3b55)
![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/99a33390-fa11-4ade-a19f-e93bcd7aaec9)
![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/440797bd-53cb-49c1-b18d-89776864c3e7)
![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/81575a16-26b2-46f1-a8ac-27c9ed0a0fe5)

<hr>
<h2>Result:</h2>
<hr>
Thus, Alpha-Beta pruning enhance the efficiency of the Minimax algorithm by reducing the number of nodes evaluated in the game tree, allowing for faster decision-making while still ensuring the optimal move is found.
