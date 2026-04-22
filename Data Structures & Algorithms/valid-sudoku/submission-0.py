class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        num = board[box_row * 3 + row][box_col * 3 + col]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)

        return True
