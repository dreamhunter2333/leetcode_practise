#
# @lc app=leetcode.cn id=1226 lang=python3
#
# [1226] 哲学家进餐
#

# @lc code=start
import threading
from collections.abc import Callable


class DiningPhilosophers:

    def __init__(self):
        self.locks = [threading.Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        right = philosopher
        left = (philosopher + 1) % 5

        if philosopher % 2 == 0:
            self.locks[right].acquire()
            self.locks[left].acquire()
        else:
            self.locks[left].acquire()
            self.locks[right].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()

        self.locks[right].release()
        self.locks[left].release()

# @lc code=end
