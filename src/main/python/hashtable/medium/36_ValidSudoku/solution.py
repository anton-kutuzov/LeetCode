from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = list()

        for i in range(0, 9):
            rows[i] = set()
            cols[i] = set()

        for i in range(0, 3):
            boxes.append(list())
            for j in range(0, 3):
                boxes[i].append(set())

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])

                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])

                box_i = i // 3
                box_j = j // 3

                if board[i][j] in boxes[box_i][box_j]:
                    return False
                else:
                    boxes[box_i][box_j].add(board[i][j])

        return True


if __name__ == '__main__':
    solution = Solution()
    assert solution.isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
    assert solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                      , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                      , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                      , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                      , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                      , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                      , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                      , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                      , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) == False
