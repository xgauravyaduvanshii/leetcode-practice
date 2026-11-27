class _Bucket:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        # My thinking: keep one bucket per count, linked in order,
        # so the ends always hold the min and max keys.
        self.head = _Bucket(0)
        self.tail = _Bucket(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_count = {}
        self.count_bucket = {}

    def _add_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        old = self.key_count.get(key, 0)
        new = old + 1
        self.key_count[key] = new
        if old:
            node = self.count_bucket[old]
            node.keys.discard(key)
            if not node.keys:
                # Old bucket is gone: the new one takes its place.
                prev_node = node.prev
                self._remove(node)
                del self.count_bucket[old]
            else:
                # Old bucket survives: the new one goes right after it.
                prev_node = node
        else:
            prev_node = self.head
        if new in self.count_bucket:
            self.count_bucket[new].keys.add(key)
        else:
            new_node = _Bucket(new)
            new_node.keys.add(key)
            self.count_bucket[new] = new_node
            self._add_after(prev_node, new_node)

    def dec(self, key: str) -> None:
        old = self.key_count[key]
        new = old - 1
        node = self.count_bucket[old]
        node.keys.discard(key)
        prev_node = node.prev
        if not node.keys:
            self._remove(node)
            del self.count_bucket[old]
        if new == 0:
            del self.key_count[key]
        else:
            self.key_count[key] = new
            if new in self.count_bucket:
                self.count_bucket[new].keys.add(key)
            else:
                new_node = _Bucket(new)
                new_node.keys.add(key)
                self.count_bucket[new] = new_node
                self._add_after(prev_node, new_node)

    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.keys))
