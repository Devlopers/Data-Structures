import sys


def recursive_linear_search(input_list, target, index=0):
    print(input_list, target, index)
    if index >= len(input_list):
        print("Target not found.")
    else:
        if input_list[index] == target:
            print(index)
            return index
        else:
            return recursive_linear_search(input_list, target, index+1)


if __name__ == '__main__':
    recursive_linear_search(sys.argv[1:-1], sys.argv[-1])
