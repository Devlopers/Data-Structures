from binarysearchtree import BinarySearchTree


def bubble_sort(orig_list):
    source = orig_list
    for index1 in range(0, len(source)):
        for index2 in range(0, len(source)):
            if index2 < len(source) - 1:
                if source[index2] > source[index2 + 1]:
                    source[index2], source[index2 + 1] = source[index2 + 1], source[index2]
    return source


def selection_sort(orig_list):
    source = orig_list
    for index1 in range(0, len(source)):
        curr_min_index = index1
        for index2 in range(index1, len(source)):
            if source[index2] < source[curr_min_index]:
                curr_min_index = index2
        source[index1], source[curr_min_index] = source[curr_min_index], source[index1]
    return source


def insertion_sort(orig_list):
    source = orig_list
    for index in range(1, len(source)):
        current_value = source[index]
        position = index
        while position > 0 and source[position - 1] > current_value:
            source[position] = source[position - 1]
            position -= 1
        source[position] = current_value
    return source


def insertion_sort_with_binary_search(orig_list):
    source = orig_list
    for index in range(1, len(source)):
        current_value = source[index]
        insertion_index = binary_search(source, current_value)
        source[insertion_index] = current_value
    return source


def tree_sort(orig_list):
    source = orig_list
    sort_tree = BinarySearchTree()
    for index, value in enumerate(source):
        sort_tree.insert(value)
    if len(source) == 0:
        return []
    else:
        return sort_tree.items_in_order()


def test_sort(sorter):
    # TODO: Write tests for the sorting algorithms.
    unsorted_array = [2, 5, 1, 3, 4, 7, 6, 8, 9, 13, 15, 12, 11, 10, 14]
    sorted_array = sorter(unsorted_array)
    print("Sorted array: ", sorted_array)


if __name__ == '__main__':
    # sorter = bubble_sort
    # sorter = selection_sort
    # sorter = insertion_sort
    # sorter = insertion_sort_with_binary_search
    sorter = tree_sort
    test_sort(sorter)
