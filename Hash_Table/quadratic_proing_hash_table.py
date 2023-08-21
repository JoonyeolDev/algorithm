class QuadraticProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def _resize(self, new_size):
        old_keys = self.keys
        old_values = self.values
        self.size = new_size
        self.keys = [None] * new_size
        self.values = [None] * new_size
        self.count = 0

        for key, value in zip(old_keys, old_values):
            if key is not None:
                self.set(key, value)

    def set(self, key, value):
        index = self._hash(key)
        original_index = index
        distance = 1

        while self.keys[index] is not None and self.keys[index] != key:
            index = (original_index + distance ** 2) % self.size
            distance += 1
            if distance > self.size:  # 전체 해시 테이블을 순회했으면 리사이징
                self._resize(2 * self.size)
                self.set(key, value)
                return

        if self.keys[index] is None:
            self.count += 1

        self.keys[index] = key
        self.values[index] = value

        if self.count > self.size // 2:
            self._resize(2 * self.size)

    def get(self, key):
        index = self._hash(key)
        original_index = index
        distance = 1

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (original_index + distance ** 2) % self.size
            distance += 1
            if distance > self.size:
                break

        return None

    def __str__(self):
        return "{"+", ".join([f"{k} : {v}" for k, v in zip(self.keys, self.values) if k is not None])+"}"


# 제곱 탐사 해시 테이블 테스트
test = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lime", "mango"]
quadratic_hash_table = QuadraticProbingHashTable()
for idx, value in enumerate(test):
    quadratic_hash_table.set(value, idx)

print(quadratic_hash_table)
# 6, 11 번째 set에서 리사이징이 일어난다. 10(default) > 20 > 40
print(quadratic_hash_table.size)