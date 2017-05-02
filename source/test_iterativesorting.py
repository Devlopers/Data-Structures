import unittest
from iterativesorting import bubble_sort, selection_sort, insertion_sort, tree_sort


class TestIterativeSort(unittest.TestCase):
    def test_empty_list(self):
        test_list = []
        assert bubble_sort(test_list) == []
        assert selection_sort(test_list) == []
        assert insertion_sort(test_list) == []
        assert tree_sort(test_list) == []

    def test_bubble_sort(self):
        test_list = [9, 5, 7, 1, 2, 4, 3, 0, 6, 8]
        assert bubble_sort(test_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_selection_sort(self):
        test_list = [9, 5, 7, 1, 2, 4, 3, 0, 6, 8]
        assert selection_sort(test_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_insertion_sort(self):
        test_list = [9, 5, 7, 1, 2, 4, 3, 0, 6, 8]
        assert insertion_sort(test_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_tree_sort(self):
        test_list = [9, 5, 7, 1, 2, 4, 3, 0, 6, 8]
        assert tree_sort(test_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
