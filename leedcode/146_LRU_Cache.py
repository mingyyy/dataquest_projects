class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.pos = {}

    def pos_key(self, last: bool) -> int:
            # last = True -> get key with the highest score (last used)
            # last = False -> get the least recent used key

            if len(self.pos) > 0:
                sorted_pos = sorted(self.pos.items(), key=lambda kv: kv[1])
                if last is True:
                    highest_score = sorted_pos[-1][1]
                    return highest_score
                else:
                    key = sorted_pos[0][0]
                    return key
            else:
                return 0

    def get(self, key: int) -> int:
        if key in self.cache:
            k = self.pos_key(last=True)
            self.pos[key] = k + 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            least_key = self.pos_key(last=False)
            self.cache[key] = self.cache.pop(least_key)
            self.pos[key] = self.pos.pop(least_key)
        k = self.pos_key(last=True)
        self.pos[key] = k + 1
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]