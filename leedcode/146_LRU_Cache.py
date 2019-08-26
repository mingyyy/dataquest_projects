class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.pos = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.pos[key] += 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # initiate
        if len(self.cache) < self.capacity:
            self.cache[key] = value
            self.pos[key] = 0
        else:
            sorted_pos = sorted(self.pos.items(), key=lambda kv: kv[1])
            k = sorted_pos[0][0]
            print(k, sorted_pos)

            del self.cache[k]
            del self.pos[k]
            self.cache[key] = value
            self.pos[key] = 0

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]