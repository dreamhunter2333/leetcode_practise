#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.post = None


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.size = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.post = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self.del_node(node)
        self.add_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node:
            self.del_node(node)
            del self.map[key]
            del node
        elif self.size == len(self.map):
            node = self.head.post
            self.del_node(node)
            del self.map[node.key]
            del node
        node = Node(key, value)
        self.add_node(node)
        self.map[key] = node

    def add_node(self, node: 'Node'):
        last_node = self.tail.pre
        last_node.post = node
        node.pre = last_node
        self.tail.pre = node
        node.post = self.tail

    def del_node(self, node: 'Node'):
        pre_node = node.pre
        post_node = node.post
        pre_node.post = post_node
        post_node.pre = pre_node

    def __repr__(self):
        res = []
        node = self.head.post
        while node.post:
            res.append(str(node.key) + '=' + str(node.value))
            node = node.post
        return repr(res)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# obj.put(1, 1)
# print(obj)
# obj.put(2, 2)
# print(obj)
# obj.get(1)
# print(obj)
# obj.put(3, 3)
# print(obj)
# obj.get(2)
# print(obj)
# obj.put(4, 4)
# print(obj)
# obj.get(1)
# print(obj)
# obj.get(3)
# print(obj)
# obj.get(4)
# print(obj)

# @lc code=end
