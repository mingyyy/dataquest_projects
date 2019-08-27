class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.pos = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            sorted_pos = sorted(self.pos.items(), key=lambda kv: kv[1])
            k = sorted_pos[min(self.capacity, len(self.cache)) - 1][1]
            self.pos[key] = k + 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if len(self.cache) < self.capacity:
            if len(self.pos) == 0:
                self.pos[key] = len(self.cache)
            else:
                sorted_pos = sorted(self.pos.items(), key=lambda kv: kv[1])
                self.pos[key] = sorted_pos[min(self.capacity, len(self.cache)) - 1][1] + 1
            self.cache[key] = value
        else:

            sorted_pos = sorted(self.pos.items(), key=lambda kv: kv[1])
            k = sorted_pos[0][0]
            self.pos[key] = sorted_pos[min(self.capacity, len(self.cache)) - 1][1] + 1
            if key not in self.cache:
                del self.cache[k]
                del self.pos[k]
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]