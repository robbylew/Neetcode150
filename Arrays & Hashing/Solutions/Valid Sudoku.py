# https://leetcode.com/problems/valid-sudoku/description/
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)  # Dictionary to track numbers in each column
        rows = collections.defaultdict(set)  # Dictionary to track numbers in each row
        squares = collections.defaultdict(set)  # Dictionary to track numbers in each 3x3 square, key is (r / 3, c / 3)

        for r in range(9):  # Iterate over each row
            for c in range(9):  # Iterate over each column in the row
                if board[r][c] == ".":  # Skip empty cells
                    continue
                if (
                    board[r][c] in rows[r] or  # Check if the number already exists in the current row
                    board[r][c] in cols[c] or  # Check if the number already exists in the current column
                    board[r][c] in squares[(r // 3, c // 3)]  # Check if the number already exists in the current 3x3 square
                ):
                    return False  # If the number is already present in row, column, or square, the board is invalid
                cols[c].add(board[r][c])  # Add the number to the current column's set
                rows[r].add(board[r][c])  # Add the number to the current row's set
                squares[(r // 3, c // 3)].add(board[r][c])  # Add the number to the current 3x3 square's set

        return True  # If no duplicates are found, the board is valid

