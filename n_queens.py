import time


class QueensSolver:
    def __init__(self, n):
        self.n = n
        self.result = [-1 for _ in range(n)]
        self.under_attack = [[0 for j in range(n)] for j in range(n)]
        self.row_available_space = [n for i in range(n)]
        self.q_min = self.n + 1

    def solve(self):
        return self.backtrack(self.n)

    def backtrack(self, q):
        if q == 0:
            return True

        # ----- Minimum Remaining Value ----- #
        mrv_index = -1
        for i in range(self.n):
            if self.result[i] == -1 and (mrv_index == -1 or self.row_available_space[i] < self.row_available_space[mrv_index]):
                mrv_index = i

        # ----- Degree heuristic (Not Exactly!) ----- #
        cells = []
        for j in range(self.n):
            if self.under_attack[mrv_index][j] != 0:
                continue
            cells.append(j)
        cells.sort(key=lambda x: abs(x - self.n/2))

        for jp in range(len(cells)):
            j = cells[jp]
            self.place_queen(mrv_index, j)
            if self.forward_check() and self.backtrack(q-1):
                return True
            self.retrieve_queen(mrv_index, j)

        return False

    def place_queen(self, i, j):
        self.result[i] = j
        self.under_attack[i][j] = 1
        self.row_available_space[i] -= 1
        self.update_under_attack(i, j, 1)

    def retrieve_queen(self, i, j):
        self.result[i] = -1
        self.under_attack[i][j] = 0
        self.row_available_space[i] += 1
        self.update_under_attack(i, j, -1)

    def update_under_attack(self, i, j, number):
        # Plus
        for x in range(self.n):
            if i != x:  # Column
                self.under_attack[x][j] += number
                self.update_row_availability(x, j, number)
            if j != x:  # Row
                self.under_attack[i][x] += number
                self.update_row_availability(i, x, number)
        # Backslash
        for x in range(-min(i, j), self.n - max(i, j)):
            if i + x != i or j + x != j:
                self.under_attack[i + x][j + x] += number
                self.update_row_availability(i + x, j + x, number)
        # Slash
        for x in range(-min(i, self.n - 1 - j), 1 + min(self.n - 1 - i, j)):
            if i + x != i or j + x != j:
                self.under_attack[i + x][j - x] += number
                self.update_row_availability(i + x, j - x, number)

    def update_row_availability(self, i, j, number):
        if number == 1 and self.under_attack[i][j] == 1:
            self.row_available_space[i] -= 1
        if number == -1 and self.under_attack[i][j] == 0:
            self.row_available_space[i] += 1

    def forward_check(self):
        for r in range(self.n):
            if self.result[r] == -1 and self.row_available_space[r] == 0:
                return False

        return True

    def print_queens(self):
        for col in self.result:
            if col == -1:
                print("_"*self.n)
            else:
                print("_"*col + "O" + "_"*(self.n-col-1))


# ----- Prints Duration times for different n values ----- #
def print_durations(n_values):
    for n in n_values:
        queen_solver = QueensSolver(n)
        start_time = time.time()
        queen_solver.solve()
        end_time = time.time()
        print("n = {} => Duration time: {}".format(n, end_time - start_time))

# ----- answer an duration time for a single n value ----- #
def solve_n_queens(n):
    queen_solver = QueensSolver(n)
    queen_solver.solve()
    queen_solver.print_queens()


print_durations([5, 20, 40, 100, 200, 300, 400, 600, 700, 800])
solve_n_queens(20)
