import tkinter as tk
from tkinter import messagebox

# Define the Sudoku solver functions
def print_grid(grid):
    return "\n".join([" ".join(str(num) if num != 0 else '.' for num in row) for row in grid])

def is_valid(grid, row, col, num):
    # Check if the number is not repeated in the current row
    if num in grid[row]:
        return False
    # Check if the number is not repeated in the current column
    if num in [grid[r][col] for r in range(9)]:
        return False
    # Check if the number is not repeated in the 3x3 box
    start_row, start_col = row - row % 3, col - col % 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False
    return True

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def solve_sudoku(grid):
    empty = find_empty_location(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

# Define the Tkinter application
class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for row in range(9):
            for col in range(9):
                entry = tk.Entry(frame, width=2, font=('Arial', 18), justify='center', borderwidth=1, relief='solid')
                entry.grid(row=row, column=col, padx=5, pady=5)
                self.entries[row][col] = entry

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.pack(pady=10)

        self.message_label = tk.Label(self.root, text="", font=('Arial', 12))
        self.message_label.pack(pady=10)

    def solve(self):
        grid = [[0 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                value = self.entries[row][col].get()
                if value:
                    try:
                        grid[row][col] = int(value)
                    except ValueError:
                        grid[row][col] = 0

        if solve_sudoku(grid):
            self.update_grid(grid)
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists.")

    def update_grid(self, grid):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(grid[row][col]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
