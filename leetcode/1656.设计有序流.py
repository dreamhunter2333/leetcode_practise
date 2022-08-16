#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#
from typing import List


# @lc code=start
class Node:
    def __init__(self) -> None:
        pass


class OrderedStream:

    def __init__(self, n: int):
        self.size = n
        self.arr = [""] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        res = []
        for i in range(self.ptr, self.size):
            if not self.arr[i]:
                break
            res.append(self.arr[i])
            self.ptr += 1
        return res


# @lc code=end
o = OrderedStream(5)
for i, v in [[3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]:
    print(o.insert(i, v))
