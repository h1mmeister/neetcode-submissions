class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        val = self.hash_map.pop(key)
        self.hash_map[key] = val
        return val
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map.pop(key)
        else:
            if len(self.hash_map) == self.capacity:
                del self.hash_map[next(iter(self.hash_map))]
        self.hash_map[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)