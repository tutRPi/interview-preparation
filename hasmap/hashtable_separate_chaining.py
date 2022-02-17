from typing import Optional


class Entry:
    def __init__(self, key: str, value):
        self.key = key
        self.value = value
        self.hashCode = hash(key)

    def __eq__(self, other) -> bool:
        if self.hashCode != other.hashCode:
            return False
        return self.key == other.key

    def __str__(self):
        return self.key + " => " + self.value


class HashTableSeparateChaining:
    __default_capacity: int = 5
    __default_load_factor: float = 0.75

    def __init__(self, capacity: int = __default_capacity, max_load_factor: float = __default_load_factor):
        if capacity <= 0:
            raise Exception("Capacity too small")
        if max_load_factor <= 0:
            raise Exception("max_load_factor invalid")
        self.__capacity: int = max(self.__default_capacity, capacity)
        self.__max_load_factor: float = max_load_factor
        self.__threshold: int = int(self.__capacity * self.__max_load_factor)
        self.__size: int = 0
        self.__table: [[Entry]] = [[]] * self.__capacity  # 2d array, alternatively linked list, binary tree, etc

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.size() == 0

    def clear(self) -> None:
        self.__table = []
        self.__size = 0

    def __normalize_index(self, key_hash: int) -> int:
        return (key_hash & 0x7FFFFFFF) % self.__capacity

    def has_key(self, key: str):
        idx = self.__normalize_index(hash(key))
        return self.__bucket_seek_entry(idx, key) is not None

    def __bucket_seek_entry(self, idx: int, key: str) -> Optional[Entry]:
        arr = self.__table[idx]
        if len(arr) == 0:
            return None
        e: Entry
        for e in arr:
            if e.key == key:
                return e
        return None

    def __bucket_insert_entry(self, idx: int, entry: Entry):
        arr = self.__table[idx]
        existing_entry: Entry = self.__bucket_seek_entry(idx, entry.key)
        if existing_entry is None:
            arr.append(entry)
            self.__size += 1
            if self.__size > self.__threshold:
                self.__resize_table()
            return None
        else:
            old_val = existing_entry.value
            existing_entry.value = entry.value
            return old_val

    def __bucket_remove_entry(self, idx: int, key: str):
        entry: Entry = self.__bucket_seek_entry(idx, key)
        if entry is not None:
            arr = self.__table[idx]
            for i, e in enumerate(arr):
                if e.key == key:
                    del self.__table[idx][i]
                    break
            self.__size -= 1
            return entry.value
        return None

    def insert(self, key: str, value):
        entry: Entry = Entry(key, value)
        idx: int = self.__normalize_index(hash(key))
        return self.__bucket_insert_entry(idx, entry)

    def get(self, key: str):
        idx: int = self.__normalize_index(hash(key))
        entry: Entry = self.__bucket_seek_entry(idx, key)
        if entry is not None:
            return entry.value
        return None

    def remove(self, key: str):
        idx: int = self.__normalize_index(hash(key))
        return self.__bucket_remove_entry(idx, key)

    def __resize_table(self):
        self.__capacity *= 2
        self.__threshold = int(self.__capacity * self.__max_load_factor)
        new_table: [[Entry]] = [[]] * self.__capacity
        for i in range(len(self.__table)):
            if len(self.__table[i]) != 0:
                e: Entry
                for e in self.__table[i]:
                    idx = self.__normalize_index(e.hashCode)
                    new_table[idx].append(e)
                self.__table[i] = []
        self.__table = new_table


hashmap = HashTableSeparateChaining(5, 0.5)
assert hashmap.is_empty() is True
hashmap.insert("foo", "bar")
hashmap.insert("test", "example")
assert hashmap.size() == 2
assert hashmap.is_empty() is False
assert hashmap.get("test") == "example"

hashmap.insert("test2", "example2")
hashmap.insert("test3", "example3")
hashmap.insert("test4", "example4")
hashmap.insert("test5", "example5")
assert hashmap.size() == 6
assert hashmap.get("test5") == "example5"
assert hashmap.remove("foo") == "bar"
assert hashmap.size() == 5
