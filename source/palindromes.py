#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string
import re


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    text = re.sub('[^0-9a-zA-Z]+', '', text.lower())
    if text == text[::-1]:
        return True
    return False
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if left is None and right is None:
        text = re.sub('[^0-9a-zA-Z]+', '', text.lower())
        left = 0
        right = len(text) - 1
    else:
        left = left + 1
        right = right - 1
    if left >= right:
        return True
    elif text[left] == text[right]:
        return is_palindrome_recursive(text, left, right)
    else:
        return False
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def is_permutation_palindrome_iterative(text):
    # TODO: implement the is_permutation_palindrome iteratively
    pass


def is_permutation_palindrome_recursive(text):
    # TODO: implement the is_permutation_palindrome recursively
    pass


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
