import io

if __name__ == '__main__':
    data = io.open('day01_input.txt', 'r').read()
    data_lines = data.split('\n')

    last_line = None
    increased = 0

    for line in data_lines:
        current_line = int(line)
        if last_line is not None and current_line > last_line:
            increased += 1

        last_line = current_line

    print(f'Result {increased}')
