import unittest
from HashTable import HashTable


class ObjectWithSettableHash(object):
    def __init__(self, value, hash_value):
        self.value = value
        self.hash_value = hash_value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self.hash_value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.value}@{self.hash_value}"


class HashTableTests(unittest.TestCase):

    def test_basic_add_get(self):
        ht = HashTable()

        ht.add('1', 'one')
        ht.add('2', 'two')
        ht.add('3', 'three')

        self.assertEqual(ht.get('1'), 'one')
        self.assertEqual(ht.get('2'), 'two')
        self.assertEqual(ht.get('3'), 'three')

    def test_colision(self):
        ht = HashTable()

        o1 = ObjectWithSettableHash('one', 1)
        o2 = ObjectWithSettableHash('two', 2)
        o3 = ObjectWithSettableHash('three', 2)

        ht.add(o1, 'one')
        # for i, e in enumerate(ht._buckets):
        #     if e is not None:
        #         print(f"{i}\t{e}")
        # print()

        ht.add(o2, 'two')
        # for i, e in enumerate(ht._buckets):
        #     if e is not None:
        #         print(f"{i}\t{e}")
        # print()

        ht.add(o3, 'three')

        # for i, e in enumerate(ht._buckets):
        #     if e is not None:
        #         print(f"{i}\t{e}")
        # print()

        self.assertEqual(ht.get(o1), 'one')
        self.assertEqual(ht.get(o2), 'two')
        self.assertEqual(ht.get(o3), 'three')

    def test_exceeding_capacity(self):
        ht = HashTable()
        ht._n_buckets = 2
        ht._buckets = [None] * 2

        ht.add('k1', 'one')
        ht.add('k2', 'two')
        ht.add('k3', 'three')

        self.assertEqual(ht.get('k1'), 'one')
        self.assertEqual(ht.get('k2'), 'two')
        self.assertEqual(ht.get('k3'), 'three')
