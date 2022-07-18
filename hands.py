# 69368294

def calculate_points(k, matrix: str):
    numbers = []
    scores = 0
    for i in range(1, 10):
        count = matrix.count(str(i))
        numbers.append(count)
    for i, elem in enumerate(numbers):
        if elem == 0:
            continue
        if int(elem) <= k:
            scores += 1
    return scores


def r_input():
    k = int(input()) * 2
    matrix = ''.join([input() for i in range(4)])
    return k, matrix


if __name__ == '__main__':
    print(calculate_points(*r_input()))
