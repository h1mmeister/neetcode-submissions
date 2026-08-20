class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.remove_from_list(node)
            self.insert_into_list(node)
            return node.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.remove_from_list(node)
            self.insert_into_list(node)
            node.value = value
        else:
            if len(self.hash_map) >= self.capacity:
                self.remove_from_tail()
            node = ListNode(key, value)
            self.hash_map[key] = node
            self.insert_into_list(node)

    def insert_into_list(self, node):
        old_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = old_node
        old_node.prev = node

    def remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_from_tail(self):
        node = self.tail.prev
        del self.hash_map[node.key]
        self.remove_from_list(node)


        
