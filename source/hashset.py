#!python
from hashtable import HashTable


class HashSet(object):

    def __init__(self, elements=None):
        """Initialize this hash set with the given initial elements"""
        self.set = HashTable()
        self.size = 0  # Count number of entries
        if elements:
            # TODO: Run 'add' for each element
            for element in elements:
                self.add(element)

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        keys = ['{}'.format(repr(k)) for k in self.set.keys()]
        return '{' + ', '.join(keys) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashSet({})'.format(repr(self.set.keys()))

    def contains(self, element):
        # TODO: Check if element present.
        # LinkedList contains: O(n)
        return self.set.contains(element)

    def add(self, element):
        # TODO: Check if element present, if not, add it.
        # LinkedList contains: O(n)
        # LinkedList append: O(1)
        if self.set.contains(element):
            pass
        else:
            self.size += 1
            self.set.set(element, None)

    def remove(self, element):
        # TODO: Check if element is present. If it is, delete it.
        # LinkedList contains: O(n)
        # LinkedList delete: O(n)
        if self.set.contains(element):
            self.size -= 1
            self.set.delete(element)
        else:
            raise KeyError('Element not found: {}'.format(element))

    def union(self, other_set):
        # TODO: Combine self with other_set.
        new_set = HashSet()
        # O(n) because HashTable keys() is O(n)
        self_keys = self.set.keys()
        # O(n) because HashTable keys() is O(n)
        other_set_keys = other_set.set.keys()
        # Add elements from other_set to new_set.
        # for loop is O(n)
        for element in other_set_keys:
            new_set.add(element)
        # Add elements from other_set to new_set.
        # for loop is O(n)
        for element in self_keys:
            new_set.add(element)
        return new_set

    def intersection(self, other_set):
        # TODO: Check for elements present in self and other_set
        new_set = HashSet()
        # O(n) because HashTable keys() is O(n)
        self_keys = self.set.keys()
        # O(n) because HashTable keys() is O(n)
        other_set_keys = other_set.set.keys()
        # Check for elements in other_set in self.
        # for loop is O(n)
        for element in other_set_keys:
            if element in self_keys:
                new_set.add(element)
            continue
        # Check for elements in other_set in self.
        # for loop is O(n)
        for element in self_keys:
            if element in other_set_keys:
                new_set.add(element)
            continue
        return new_set

    def difference(self, other_set):
        # TODO: Check for elements that differ between set and other_set
        new_set = HashSet()
        # O(n) because HashTable keys() is O(n)
        self_keys = self.set.keys()
        # O(n) because HashTable keys() is O(n)
        other_set_keys = other_set.set.keys()
        # Check for elements in other_set not in self.
        # for loop is O(n)
        for element in other_set_keys:
            if element not in self_keys:
                new_set.add(element)
            continue
        # Check for elements in self not in other_set.
        # for loop is O(n)
        for element in self_keys:
            if element not in other_set_keys:
                new_set.add(element)
            continue
        return new_set

    def is_subset(self, other_set):
        # TODO: Check if other_set is a subset of self
        # O(n) because union is O(n)
        return self.union(other_set).size == self.size


def test_hash_set():
    hs = HashSet()
    print('HashSet: ' + str(hs.set))

    print('Setting entries:')
    hs.add('I')
    print('add(I): ' + str(hs))
    hs.add('V')
    print('add(V): ' + str(hs))
    print('size: ' + str(hs.size))
    hs.add('X')
    print('add(X): ' + str(hs))
    hs.add('L')  # Should trigger resize
    print('add(L): ' + str(hs))
    print('size: ' + str(hs.size))

    print('Contains entries: ')
    print('contains(X): ' + str(hs.contains('X')))
    print('contains(Z): ' + str(hs.contains('Z')))

    print('Deleting entries:')
    hs.remove('I')
    print('remove(I): ' + str(hs))
    hs.remove('V')
    print('remove(V): ' + str(hs))
    hs.remove('X')
    print('remove(X): ' + str(hs))
    hs.remove('L')
    print('remove(L): ' + str(hs))
    print('contains(X): ' + str(hs.contains('X')))
    print('size: ' + str(hs.size))


if __name__ == '__main__':
    test_hash_set()
