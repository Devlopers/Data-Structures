import sys


def recursive_binary_search(input_list, target, iterations=1, curr_index=0):
    # print(input_list, target, iterations, curr_index)
    iterations += 1
    if curr_index >= len(input_list) or iterations > len(input_list):
        print("Target not found.")
        return None
    elif input_list[curr_index] == target:
        print("On target!")
        print(curr_index)
        return curr_index
    else:
        # print("Step:", len(input_list)//iterations)
        if input_list[curr_index] < target:
            # print("Less than target.")
            new_index = curr_index + (len(input_list) - 1)//iterations
            # print(new_index)
            # print(input_list[new_index])
            recursive_binary_search(input_list, target, iterations, new_index)
        else:
            # print("Greater than target.")
            new_index = curr_index - (len(input_list) - 1)//iterations
            # print(new_index)
            # print(input_list[new_index])
            recursive_binary_search(input_list, target, iterations, new_index)


if __name__ == '__main__':
    recursive_binary_search(sys.argv[1:-1], sys.argv[-1])
