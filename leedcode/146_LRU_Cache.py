class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.pos = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            base_value = 0
            for v in self.pos.values():
                if v > base_value:
                    base_value = v
            self.pos[key] = base_value + 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == 0:
            self.cache[key] = value
            self.pos[key] = 0
        else:
            counter = 0
            for k, v in self.pos.items():
                if counter == 0:
                    low, high, low_key = v, v, k
                else:
                    if v > high:
                        high = v
                    if v < low:
                        low = v
                        low_key = k
                counter += 1

            if key in self.cache:
                self.cache[key] = value
                self.pos[key] = high + 1
            else:
                if len(self.cache) < self.capacity:
                    self.cache[key] = value
                    self.pos[key] = high + 1
                else:
                    self.cache[key] = self.cache.pop(low_key)
                    self.pos[key] = self.pos.pop(low_key)
                    self.cache[key] = value
                    self.pos[key] = high + 1

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