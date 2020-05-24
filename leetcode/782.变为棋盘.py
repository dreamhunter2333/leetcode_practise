#
# @lc app=leetcode.cn id=782 lang=python3
#
# [782] 变为棋盘
#
# https://leetcode-cn.com/problems/transform-to-chessboard/description/
#
# algorithms
# Hard (39.73%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    586
# Total Submissions: 1.4K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]'
#
# 一个 N x N的 board 仅由 0 和 1 组成 。每次移动，你能任意交换两列或是两行的位置。
# 
# 输出将这个矩阵变为 “棋盘” 所需的最小移动次数。“棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。如果不存在可行的变换，输出 -1。
# 
# 示例:
# 输入: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# 输出: 2
# 解释:
# 一种可行的变换方式如下，从左到右：
# 
# 0110     1010     1010
# 0110 --> 1010 --> 0101
# 1001     0101     1010
# 1001     0101     0101
# 
# 第一次移动交换了第一列和第二列。
# 第二次移动交换了第二行和第三行。
# 
# 
# 输入: board = [[0, 1], [1, 0]]
# 输出: 0
# 解释:
# 注意左上角的格值为0时也是合法的棋盘，如：
# 
# 01
# 10
# 
# 也是合法的棋盘.
# 
# 输入: board = [[1, 0], [1, 0]]
# 输出: -1
# 解释:
# 任意的变换都不能使这个输入变为合法的棋盘。
# 
# 
# 
# 
# 提示：
# 
# 
# board 是方阵，且行列数的范围是[2, 30]。
# board[i][j] 将只包含 0或 1。
# 
# 
#

# @lc code=start
from typing import List
import collections

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        """
        TODO: transform
        """
        N = len(board)
        ans = 0
        # For each count of lines from {rows, columns}...
        for count in (collections.Counter(map(tuple, board)),
                      collections.Counter(zip(*board))):

            # If there are more than 2 kinds of lines,
            # or if the number of kinds is not appropriate ...
            if len(count) != 2 or sorted(count.values()) != [N//2, (N+1)//2]:
                return -1

            # If the lines are not opposite each other, impossible
            line1, line2 = count
            if not all(x ^ y for x, y in zip(line1, line2)):
                return -1

            # starts = what could be the starting value of line1
            # If N is odd, then we have to start with the more
            # frequent element
            starts = [+(line1.count(1) * 2 > N)] if N%2 else [0, 1]

            # To transform line1 into the ideal line [i%2 for i ...],
            # we take the number of differences and divide by two
            # TODO: 看不懂
            ans += min(sum((i-x) % 2 for i, x in enumerate(line1, start))
                       for start in starts) / 2

        return int(ans)


if __name__ == "__main__":
    print(Solution().movesToChessboard([[1,1,0],[0,0,1],[0,0,1]]))

# @lc code=end
