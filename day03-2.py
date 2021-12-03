import io


def most_common(data, position):
    count = {'0': 0, '1': 0}
    for d in data:
        count[d[position]] += 1

    if count['0'] > count['1']:
        return '0'
    return '1'


def least_common(data, position):
    count = {'0': 0, '1': 0}
    for d in data:
        count[d[position]] += 1

    if count['0'] <= count['1']:
        return '0'
    return '1'


if __name__ == '__main__':
    data = io.open('day03_input.txt', 'r').read()
    data_lines = data.split('\n')

    data_oxygen = data_lines.copy()
    data_co2 = data_lines.copy()

    pos = -1
    while len(data_oxygen) > 1:
        pos += 1
        target = most_common(data_oxygen, pos)
        data_oxygen = [num for num in data_oxygen if num[pos] == target]

    pos = -1
    while len(data_co2) > 1:
        pos += 1
        target = least_common(data_co2, pos)
        data_co2 = [num for num in data_co2 if num[pos] == target]

    print(int(data_oxygen[0], 2) * int(data_co2[0], 2))
