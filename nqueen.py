class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self, row=0):
        if row == self.n:
            # If all queens are placed
            solution = ["".join(' Q ' if cell == 1 else ' * ' for cell in row) for row in self.board]
            self.solutions.append(solution)
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(row + 1)
                self.board[row][col] = 0

    def get_solutions(self):
        self.solve()
        return self.solutions


n = int(input("Enter the size of the chessboard (N): "))
n_queens = NQueens(n)
solutions = n_queens.get_solutions()

print(f"Number of solutions for {n}-queens problem: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()
