# 69368294

# Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
# В нём на каждом раунде появляется конфигурация цифр и точек.
# На клавише написана либо точка, либо цифра от 1 до 9.
# В момент времени t игрок должен одновременно нажать на все клавиши,
# на которых написана цифра t.
# Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
# Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.
# Найдите число баллов, которое смогут заработать Гоша и Тимофей,
# если будут нажимать на клавиши вдвоём.

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
