class HashTableEntry(object):
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"key: {self.key} value: {self.value} next: {self.next}"


class HashTable(object):
    def __init__(self):
        self._n_entries = 0
        self._n_buckets = 256
        self._buckets = [None] * self._n_buckets

    def __str__(self):
        output = ""
        for i, e in enumerate(self._buckets):
            if e is not None:
                output += f"{i}\t{e}\n"
        return output

    def _expand_buckets(self):
        # Double the capacity of the buckets, update _n_buckets
        # and recalc hashes for new capacity.
        orig_buckets = self._buckets.copy()
        self._n_buckets *= 2
        self._buckets = [None] * self._n_buckets

        for entry in orig_buckets:
            self.add(entry.key, entry.value)

    def _find_next_unused_index(self, start):
        index = start
        while self._buckets[index] is not None:
            index = (index + 1) % self._n_buckets
        return index

    def get(self, key):
        index = hash(key) % self._n_buckets
        entry = self._buckets[index]

        if entry is None:
            raise Exception(f'Invalid Key: {key}')

        if entry.next is None:
            # No hash collision exists.
            return entry.value

        # Handle has colisions.
        while entry.next is not None:
            # print(f'entry: {entry}')
            if entry.key == key:
                return entry.value
            entry = self._buckets[entry.next]
        if entry.key == key:
            return entry.value
        # None of the linked entries for a hash match the key
        raise Exception(f'Invalid Key: {key}')

    def add(self, key, value):
        # print('add')
        if self._n_entries == self._n_buckets:
            self._expand_buckets()
        index = hash(key) % self._n_buckets
        entry = self._buckets[index]

        # print(f'entry: {entry}')
        # case: add a new entry (no colision)
        if entry is None:
            entry = HashTableEntry(key, value)
            self._buckets[index] = entry
            self._n_entries += 1
        else:
            if entry.key == key:
                # case: update an existing key
                entry.value = value

            else:
                # case: add a new entry (with colision)
                while entry.next is not None:
                    entry = self._buckets[entry.next]

                new_index = self._find_next_unused_index(index)
                entry.next = new_index
                new_entry = HashTableEntry(key, value)
                self._buckets[new_index] = new_entry
                self._n_entries += 1

    def delete(self, key):
        index = hash(key) % self._n_buckets
        entry = self._buckets[index]

        if entry is None:
            return

        if entry.next is None:
            # No hash colision exists.
            return

        # Handle hash colisions.
        '''
        101 k:'a' v:'AAA' n:102
        102 k:'b' v:'BBB' n:103
        103 k:'c' v:'BBB' n:None
        to:
        101 k:'a' v:'AAA' n:103
        103 k:'c' v:'BBB' n:None
        '''
        prev_entry = None
        while entry.next is not None:
            if entry.key == key:
                # Remove the entry and update the previous entry's 'next'
                if prev_entry is not None:
                    prev_entry.next = entry.next
                entry = None
                return
            entry = self._buckets[entry.next]

    def keys(self):
        # return an iteration of keys
        pass

    def items(self):
        # return an interation of all (key, item)
        pass
