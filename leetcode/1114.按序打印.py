#
# @lc app=leetcode.cn id=1114 lang=python3
#
# [1114] 按序打印
#

# @lc code=start
import threading

from typing import Callable


class Foo:
    def __init__(self):
        self.a = threading.Lock()
        self.a.acquire()
        self.b = threading.Lock()
        self.b.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.a.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.a.acquire()
        printSecond()
        self.b.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
# @lc code=end
