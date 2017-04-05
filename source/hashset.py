#!python
from hashtable import HashTable


class HashSet(object):

    def __init__(self, elements=None):
        """Initialize this hash set with the given initial elements"""
        
        self.size = 0  # Count number of entries
        if elements:
            # TODO: Run 'add' for each element
            for element in elements:
                self.add(element)

    def contains(self, element):
        # TODO: Check if element present, if not, add it.
        pass

    def add(self, element):
        # TODO: Check if element is present. If it is, delete it.
        pass

    def remove(self, element):
        # TODO: Check if element is present. If it is, delete it.
        pass

    def union(self, other_set):
        # TODO: Combine two self with another set.
        pass

    def intersection(self, other_set):
        # TODO: Check for elements present in self and other_set
        pass

    def difference(self, other_set):
        # TODO: Check for elements that differ between set and other_set
        pass

    def is_subset(self, other_set):
        # TODO: Check if other_set is a subset of self
        pass


def test_hash_set():
    hs = HashSet()
    # print('HashTable: ' + str(ht))
    #
    # print('Setting entries:')
    # ht.set('I', 1)
    # print('set(I, 1): ' + str(ht))
    # ht.set('V', 5)
    # print('set(V, 5): ' + str(ht))
    # print('size: ' + str(ht.size))
    # print('length: ' + str(ht.length()))
    # print('buckets: ' + str(len(ht.buckets)))
    # print('load_factor: ' + str(ht.load_factor()))
    # ht.set('X', 10)
    # print('set(X, 10): ' + str(ht))
    # ht.set('L', 50)  # Should trigger resize
    # print('set(L, 50): ' + str(ht))
    # print('size: ' + str(ht.size))
    # print('length: ' + str(ht.length()))
    # print('buckets: ' + str(len(ht.buckets)))
    # print('load_factor: ' + str(ht.load_factor()))
    #
    # print('Getting entries:')
    # print('get(I): ' + str(ht.get('I')))
    # print('get(V): ' + str(ht.get('V')))
    # print('get(X): ' + str(ht.get('X')))
    # print('get(L): ' + str(ht.get('L')))
    # print('contains(X): ' + str(ht.contains('X')))
    # print('contains(Z): ' + str(ht.contains('Z')))
    #
    # print('Deleting entries:')
    # ht.delete('I')
    # print('delete(I): ' + str(ht))
    # ht.delete('V')
    # print('delete(V): ' + str(ht))
    # ht.delete('X')
    # print('delete(X): ' + str(ht))
    # ht.delete('L')
    # print('delete(L): ' + str(ht))
    # print('contains(X): ' + str(ht.contains('X')))
    # print('size: ' + str(ht.size))
    # print('length: ' + str(ht.length()))
    # print('buckets: ' + str(len(ht.buckets)))
    # print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_set()
