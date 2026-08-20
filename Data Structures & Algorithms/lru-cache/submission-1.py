class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        
    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        value = self.hash_map.pop(key)
        self.hash_map[key] = value
        return value
        
    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map.pop(key)
        elif self.capacity == len(self.hash_map):
            del self.hash_map[next(iter(self.hash_map))]
        self.hash_map[key] = value
        
