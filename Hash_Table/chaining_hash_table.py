class Node:
    """연결 리스트의 노드를 위한 클래스"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0  # 저장된 요소의 수

    def _hash(self, key):
        """해시 함수: 키를 받아 해시 값을 반환합니다."""
        return hash(key) % self.size

    def set(self, key, value):
        """키-값 쌍을 저장합니다."""
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current:
                # 이미 키가 있으면 값을 갱신
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:  # 마지막 노드이면
                    current.next = Node(key, value)
                    break
                current = current.next

        self.count += 1
        # 요소 수가 테이블 크기의 절반을 초과하면 리사이징
        if self.count > self.size // 2:
            self._resize(2 * self.size)

    def get(self, key):
        """키에 해당하는 값을 반환합니다."""
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def _resize(self, new_size):
        """해시 테이블의 크기를 조정합니다."""
        old_table = self.table
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0  # 재삽입될 때 다시 계산됩니다.

        for head_node in old_table:
            current = head_node
            while current:
                self.set(current.key, current.value)
                current = current.next

    def __str__(self):
        result = []
        for head_node in self.table:
            if head_node:
                current = head_node
                while current:
                    result.append(f"{current.key} : {current.value}")
                    current = current.next
        return "{"+", ".join(result)+"}"


# 해시 테이블 테스트
test = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lime", "mango"]
hash_table = HashTable()
for idx, value in enumerate(test):
    hash_table.set(value, idx)

print(hash_table)
# 6, 11 번째 set에서 리사이징이 일어난다. 10(default) > 20 > 40
print(hash_table.size)