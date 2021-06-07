#
# @lc app=leetcode.cn id=1115 lang=python3
#
# [1115] 交替打印FooBar
#

# @lc code=start
import threading

from collections.abc import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock_a = threading.Lock()
        self.lock_b = threading.Lock()
        self.lock_b.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lock_a.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock_b.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lock_b.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock_a.release()

# @lc code=end
