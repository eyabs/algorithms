class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.value = None

    def __str__(self):
        return(f"value: {self.value} children:{[c for c in self.children]}")

    def __repr__(self):
        return self.__str__()


class Trie(object):
    '''
    1 1 1
        2
      2 3
    2 1 1
      2 1

    ([])        -> [1, 2]
    ([1])       -> [1, 2]
    ([1,1])     -> [1, 2]
    ([1,1,1])   -> []
    ([1,1,2])   -> []
    ([1,2]) -> [3]
    - >

    '''

    def __init__(self):
        self.nodes = TrieNode()

    def _collect(self, node, visited=[]):
        # print(f'_collect')
        # print(f'node:{node}')
        # print(f'visited:{visited}')
        if node is None or len(node.children) == 0:
            yield visited
        else:
            for val, child in node.children.items():
                # print(f'val:{val}')
                # print(f'child:{child}')
                new_visited = visited + [val]
                # print(f'new_visited:{new_visited}')
                yield from self._collect(child, new_visited)

    def collect(self, start_path=[]):
        start_path = list(start_path)
        '''
        1 1 1
            2
          2 3
        2 1 1
          2 1

        [] ->
            [1,1,1]
            [1,1,2]
            [1,2,3]
            [2,1,1]
            [2,2,1]

        [1,1] ->
            [1,1,1]
            [1,1,2]

        '''
        node = self.find(start_path)
        print(f'collect: start_path: {start_path}')
        print(node)
        results = [start_path + i for i in self._collect(node)]
        return results

    def collect_string(self, start_path=''):
        results = self.collect(start_path)
        results = [''.join(word) for word in results]
        return results


    def find(self, path):
        '''
        return children at the query path
        1 1 1
            2
          2 3
        2 1 1
          4 1
                       not arrays, keys to child nodes
        ([])        -> [1, 2]
        ([1])       -> [1, 2]
        ([1, 1])    -> [1, 2]
        ([1, 1, 1]) -> []
        ([1, 1, 2]) -> []
        ([1, 2])    -> [3]
        ([2])       -> [1, 4]
        ([2, 1])    -> [1]
        ([2, 4])    -> [1]
        ([3])       -> []


        '''
        current_node = self.nodes
        for val in path:
            if val not in current_node.children:
                return None
            current_node = current_node.children[val]
        return current_node

    def _insert_to_node(self, node, values):
        # print('-> _insert_to_node')
        # print(f'values:{values}')
        # print(f'node:{node}')
        # print(f'node.children:{node.children}')
        for val in values:
            # print(f'val:{val}')
            # print(f'node:{node}')
            # print(f'node.children:{node.children}')
            if val not in node.children:
                new_node = TrieNode()
                new_node.value = val
                node.children[val] = new_node
            node = node.children[val]

    def insert(self, values, path=[]):
        # print('-> insert')
        # print(f'values: {values}')
        # print(f'path: {path}')
        node = self.find(path)
        self._insert_to_node(node, values)
        # print(self.nodes)
