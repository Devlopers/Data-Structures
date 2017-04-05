#!python

from hashset import HashSet
import unittest


class HashSetTest(unittest.TestCase):

    def test_init(self):
        hs = HashSet()
        assert hs.size == 0

    def test_size(self):
        hs = HashSet()
        assert hs.size == 0
        hs.add('I')
        assert hs.size == 1
        hs.add('V')
        assert hs.size == 2
        hs.add('X')
        assert hs.size == 3

    def test_contains(self):
        hs = HashSet()
        hs.add('I')
        hs.add('V')
        hs.add('X')
        assert hs.contains('I') is True
        assert hs.contains('V') is True
        assert hs.contains('X') is True
        assert hs.contains('A') is False

    def test_add_and_contains(self):
        hs = HashSet()
        hs.add('I')
        hs.add('V')
        hs.add('X')
        assert hs.contains('I') is True
        assert hs.contains('V') is True
        assert hs.contains('X') is True
        assert hs.size == 3

    def test_add_twice_and_contains(self):
        hs = HashSet()
        hs.add('I')
        hs.add('V')
        hs.add('X')
        assert hs.size == 3
        hs.add('V')  # Update value
        hs.add('X')  # Update value
        assert hs.contains('I') is True
        assert hs.contains('V') is True
        assert hs.contains('X') is True
        assert hs.size == 3  # Check size is not overcounting

    def test_remove(self):
        hs = HashSet()
        hs.add('I')
        hs.add('V')
        hs.add('X')
        assert hs.size == 3
        hs.remove('I')
        hs.remove('X')
        assert hs.size == 1
        with self.assertRaises(KeyError):
            hs.remove('X')  # Key no longer exists
        with self.assertRaises(KeyError):
            hs.remove('A')  # Key does not exist

    def test_union(self):
        hs = HashSet(['one', 'fish', 'two', 'fish'])
        hs2 = HashSet(['red', 'fish', 'blue', 'fish'])
        hs_union = hs.union(hs2)
        assert hs_union.contains('red') is True
        assert hs_union.contains('blue') is True
        print(str(hs_union))
        assert hs_union.contains('purple') is False

    def test_intersection(self):
        hs = HashSet(['one', 'fish', 'two', 'fish'])
        hs2 = HashSet(['red', 'fish', 'blue', 'fish', 'two'])
        hs_intersect = hs.intersection(hs2)
        assert hs_intersect.contains('fish') is True
        assert hs_intersect.contains('two') is True
        print(str(hs_intersect))
        assert hs_intersect.contains('one') is False
        assert hs_intersect.contains('red') is False
        assert hs_intersect.contains('blue') is False

    def test_difference(self):
        hs = HashSet(['one', 'fish', 'two', 'fish'])
        hs2 = HashSet(['red', 'fish', 'blue', 'fish', 'two'])
        hs_difference = hs.difference(hs2)
        assert hs_difference.contains('red') is True
        assert hs_difference.contains('blue') is True
        assert hs_difference.contains('one') is True
        print(str(hs_difference))
        assert hs_difference.contains('fish') is False
        assert hs_difference.contains('two') is False

    def test_is_subset(self):
        hs = HashSet(['one', 'fish', 'two', 'fish'])
        hs2 = HashSet(['red', 'fish', 'blue', 'fish', 'two'])
        hs3 = HashSet(['one', 'fish'])
        assert hs.is_subset(hs2) is False
        assert hs.is_subset(hs3) is True


if __name__ == '__main__':
    unittest.main()
