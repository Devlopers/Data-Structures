#!python
import math


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index >= len(array):
        return None
    elif array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    curr_index = len(array)/2
    last_index = 0
    curr_value = array[curr_index]
    while curr_value != item:
        new_index = int(math.ceil(abs(curr_index - last_index) / 2.0))
        if curr_value < item:
            new_index = curr_index + new_index
        else:
            new_index = curr_index - new_index
        if curr_index <= 0 or curr_index >= len(array) - 1 or new_index == last_index:
            return None
        last_index = curr_index
        curr_index = new_index
        curr_value = array[curr_index]
    return curr_index


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left is None:
        left = 0
    if right is None:
        right = len(array)
    print("Right: ", right, "Left: ", left)
    incrementor = (right - left) / 2
    index = left + incrementor
    if index < 0 or index > len(array) - 1 or index - 1 == right or index + 1 == left:
        return None
    if array[index] == item:
        print("index", index)
        return index
    elif array[index] > item:
        return binary_search_recursive(array, item, left, index - 1)
    elif array[index] < item:
        return binary_search_recursive(array, item, index + 1, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below
