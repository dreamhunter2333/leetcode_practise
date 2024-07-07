#
# @lc app=leetcode.cn id=1958 lang=python3
#
# [1958] 检查操作是否合法
#
from typing import List

# @lc code=start


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

        def check(dx: int, dy: int) -> bool:
            x = rMove + dx
            y = cMove + dy
            first_point = True
            while 0 <= x < 8 and 0 <= y < 8:
                if first_point:
                    first_point = False
                    if board[x][y] in (".", color):
                        return False
                    continue
                if board[x][y] == ".":
                    return False
                if board[x][y] == color:
                    return True
                x += dx
                y += dy
            return False

        for dx, dy in (
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ):
            if check(dx, dy):
                return True
        return False


# @lc code=end
print(Solution().checkMove(
    [
        [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "W", ".", ".", ".", "."],
        [".", ".", ".", "W", ".", ".", ".", "."],
        [".", ".", ".", "W", ".", ".", ".", "."],
        ["W", "B", "B", ".", "W", "W", "W", "B"],
        [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "W", ".", ".", ".", "."]
    ],
    4, 3, "B"
))
