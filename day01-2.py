import io

if __name__ == '__main__':
    data = io.open('day01_input.txt', 'r').read()
    data_lines = data.split('\n')

    data_1 = int(data_lines.pop(0))
    data_2 = int(data_lines.pop(0))
    data_3 = None
    results = []

    for line in data_lines:
        data_3 = int(line)
        results.append(data_1 + data_2 + data_3)
        data_1 = data_2
        data_2 = data_3

    last_result = None
    increased = 0
    for result in results:
        if last_result is not None and result > last_result:
            increased += 1

        last_result = result

    print(f'Result {increased}')
