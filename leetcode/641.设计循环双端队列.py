#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class Node:
    def __init__(self, value: int, pre: "Node" = None, post: "Node" = None) -> None:
        self.value = value
        self.pre = pre
        self.post = post


class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.post = self.tail
        self.tail.pre = self.head

    def insertFront(self, value: int) -> bool:
        if self.size >= self.max_size:
            return False
        node = Node(value)
        post_node = self.head.post
        post_node.pre = node
        self.head.post = node
        node.post = post_node
        node.pre = self.head
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size >= self.max_size:
            return False
        node = Node(value)
        pre_node = self.tail.pre
        pre_node.post = node
        self.tail.pre = node
        node.post = self.tail
        node.pre = pre_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size <= 0:
            return False
        post_node = self.head.post
        next_node = post_node.post
        self.head.post = next_node
        next_node.pre = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size <= 0:
            return False
        pre_node = self.tail.pre
        next_node = pre_node.pre
        self.tail.pre = next_node
        next_node.post = self.tail
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size <= 0:
            return -1
        return self.head.post.value

    def getRear(self) -> int:
        if self.size <= 0:
            return -1
        return self.tail.pre.value

    def isEmpty(self) -> bool:
        return self.size <= 0

    def isFull(self) -> bool:
        return self.size == self.max_size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end
