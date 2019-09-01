from collections import OrderedDict as od

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = od()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(False)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

# ["LRUCache","put","get"]
# [[1],[2,1],[1]]

# ["LRUCache","put","put","get","put","get","put","get","get","get", "put", "put", "put", "get"]
# [[4],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4],[5,50], [3, 30], [3, 34], [5] ]


# ["LRUCache","get","put","put","get","put","put","get","get"]
# [[2],[2],[2,6],[2,5], [1],[1,5],[1,2],[1],[2]]
#
# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]