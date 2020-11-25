import unittest
from Trie import Trie


class TrieTests(unittest.TestCase):

    # Question 1

    def test_insert_trie_one(self):
        trie = Trie()

        arr1 = [1, 2, 3]

        trie.insert(arr1)
        collection = trie.collect([])
        print(collection)
        self.assertEqual([[1, 2, 3]], collection)

    def test_insert_trie_multi(self):
        trie = Trie()

        trie.insert([1, 1, 1])
        trie.insert([1, 1, 2])
        trie.insert([1, 1, 3])
        trie.insert([1, 2, 1])
        trie.insert([1, 2, 2])
        trie.insert([1, 2, 3])
        trie.insert([1, 3, 4])
        trie.insert([5, 1, 1])
        trie.insert([5, 3, 1])

        collection = trie.collect([])
        print(collection)
        self.assertEqual([
            [1, 1, 1],
            [1, 1, 2],
            [1, 1, 3],
            [1, 2, 1],
            [1, 2, 2],
            [1, 2, 3],
            [1, 3, 4],
            [5, 1, 1],
            [5, 3, 1]
        ], collection)

        collection11 = trie.collect([1, 1])
        print(collection11)
        collection5 = trie.collect([5])
        self.assertEqual([
            [1, 1, 1],
            [1, 1, 2],
            [1, 1, 3]
        ],
            collection11)
        self.assertEqual([
            [5, 1, 1],
            [5, 3, 1]
        ],
            collection5)
        print(collection5)

    def test_insert_string(self):
        trie = Trie()

        trie.insert('ant')
        trie.insert('bar')
        trie.insert('bat')
        trie.insert('car')
        trie.insert('cat')
        trie.insert('cry')

        all_words = trie.collect_string('')
        print(f'all words: {all_words}')

        self.assertEqual([
            'ant',
            'bar',
            'bat',
            'car',
            'cat',
            'cry'
        ],
            all_words)

        a_words = trie.collect_string('a')
        print(f'a words: {a_words}')

        self.assertEqual([
            'ant'
        ],
            a_words)

        b_words = trie.collect_string('b')
        print(f'b words: {b_words}')

        self.assertEqual([
            'bar',
            'bat'
        ],
            b_words)

        c_words = trie.collect_string('c')
        print(f'c words: {c_words}')

        self.assertEqual([
            'car',
            'cat',
            'cry'
        ],
            c_words)

        ca_words = trie.collect_string('ca')
        print(f'ca words: {ca_words}')

        self.assertEqual([
            'car',
            'cat'
        ],
            ca_words)

    # def test_path_exists_true(self):
    #     trie = Trie()

    #     trie.insert([1, 1, 1])
    #     trie.insert([1, 1, 2])
    #     trie.insert([1, 1, 3])
    #     trie.insert([1, 2, 1])
    #     trie.insert([1, 2, 2])
    #     trie.insert([1, 2, 3])
    #     trie.insert([1, 3, 4])
    #     trie.insert([5, 1, 1])
    #     trie.insert([5, 3, 1])

    #     self.assertTrue(trie.contains([5]))
    #     self.assertTrue(trie.contains([1,2,3]))

    # def test_path_exists_false(self):
    #     trie = Trie()

    #     trie.insert([1, 1, 1])
    #     trie.insert([1, 1, 2])
    #     trie.insert([1, 1, 3])
    #     trie.insert([1, 2, 1])
    #     trie.insert([1, 2, 2])
    #     trie.insert([1, 2, 3])
    #     trie.insert([1, 3, 4])
    #     trie.insert([5, 1, 1])
    #     trie.insert([5, 3, 1])

    #     self.assertFalse(trie.contains([4]))
    #     self.assertFalse(trie.contains([1,2,4]))
    #     self.assertFalse(trie.contains([1,2,3,4]))

    # def test_search_trie(self):
    #     pass
