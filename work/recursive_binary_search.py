import sys
import math


def recursive_binary_search(input_list, target, iterations=0, curr_index=0):
    # print(input_list, target, iterations, curr_index)
    iterations += 1
    # if curr_index is None:
    #     curr_index = len(input_list)//2
    # print("Iterations: ", iterations, math.ceil(len(input_list)/(2**iterations)), " curr_index: ", curr_index)
    if curr_index >= len(input_list) or iterations > len(input_list):
        # print("Target not found.")
        return None
    elif input_list[curr_index] == target:
        # print("On target!")
        # print(curr_index)
        return curr_index
    else:
        # print("Step:", len(input_list)//iterations)
        if input_list[curr_index] < target:
            # print("Less than target.")
            new_index = curr_index + int(math.ceil(len(input_list)/(2**iterations)))
            # print(new_index)
            # print(input_list[new_index])
            return recursive_binary_search(input_list, target, iterations, new_index)
        else:
            # print("Greater than target.")
            new_index = curr_index - int(math.ceil(len(input_list)/(2**iterations)))
            # print(new_index)
            # print(input_list[new_index])
            return recursive_binary_search(input_list, target, iterations, new_index)


if __name__ == '__main__':
    recursive_binary_search(sys.argv[1:-1], sys.argv[-1])
