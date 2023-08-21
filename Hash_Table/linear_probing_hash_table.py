class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.count = 0  # 저장된 요소의 수

    def _hash(self, key):
        """해시 함수: 키를 받아 해시 값을 반환합니다."""
        return hash(key) % self.size

    def _resize(self, new_size):
        """해시 테이블의 크기를 조정합니다."""
        old_keys = self.keys
        old_values = self.values

        self.size = new_size
        self.keys = [None] * new_size
        self.values = [None] * new_size
        self.count = 0  # 재삽입될 때 다시 계산

        for key, value in zip(old_keys, old_values):
            if key is not None:
                self.set(key, value)

    def set(self, key, value):
        """키-값 쌍을 저장합니다."""
        index = self._hash(key)
        original_index = index

        # 선형 탐사
        while self.keys[index] is not None and self.keys[index] != key:
            index = (index + 1) % self.size
            if index == original_index:  # 전체 해시 테이블을 순회했으면 리사이징
                self._resize(2 * self.size)
                self.set(key, value)
                return

        # 새로운 키 삽입 시
        if self.keys[index] is None:
            self.count += 1

        self.keys[index] = key
        self.values[index] = value

        # 요소 수가 테이블 크기의 절반을 초과하면 리사이징
        if self.count > self.size // 2:
            self._resize(2 * self.size)

    def get(self, key):
        """키에 해당하는 값을 반환합니다."""
        index = self._hash(key)
        original_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
            if index == original_index:
                break

        return None

    def __str__(self):
        return "{"+", ".join([f"{k} : {v}" for k, v in zip(self.keys, self.values) if k is not None])+"}"


# 선형 탐사 해시 테이블 테스트
test = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lime", "mango"]
linear_hash_table = LinearProbingHashTable()
for idx, value in enumerate(test):
    linear_hash_table.set(value, idx)

print(linear_hash_table)
# 6, 11 번째 set에서 리사이징이 일어난다. 10(default) > 20 > 40
print(linear_hash_table.size)