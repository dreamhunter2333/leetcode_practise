#
# @lc app=leetcode.cn id=636 lang=python3
#
# [636] 函数的独占时间
#
from typing import List


# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for log in logs:
            idx, op, timestamp = log.split(':')
            idx, timestamp = int(idx), int(timestamp)
            if op == 'start':
                if stack:
                    res[stack[-1][0]] += timestamp - stack[-1][1]
                    stack[-1][1] = timestamp
                stack.append([idx, timestamp])
            else:
                i, t = stack.pop()
                res[i] += timestamp - t + 1
                if stack:
                    stack[-1][1] = timestamp + 1
        return res


# @lc code=end
print(Solution().exclusiveTime(
    n=2, logs=["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
))
