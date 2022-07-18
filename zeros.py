# 69368837

def get_nearest_zero(len_street, homes):
    SEARCH_VALUE = 0
    index_zeros = [i for i in range(len(homes)) if homes[i] == SEARCH_VALUE]
    result_list = [0] * len_street

    for index in range(index_zeros[0]):
        result_list[index] = index_zeros[0] - index
    for index in range(len(index_zeros) - 1):
        for pos in range(index_zeros[index] + 1, index_zeros[index + 1]):
            result_list[pos] = min(
                pos - index_zeros[index], index_zeros[index + 1] - pos
                )
    for index in range(index_zeros[-1] + 1, len(homes)):
        result_list[index] = index - index_zeros[-1]
    return result_list


def init_input():
    len_street = int(input())
    homes = [int(i) for i in input().strip().split()]
    return len_street, homes


if __name__ == '__main__':
    print(*get_nearest_zero(*init_input()))
