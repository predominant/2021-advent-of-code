import io

if __name__ == '__main__':
    data = io.open('day02_input.txt', 'r').read()
    data_lines = data.split('\n')

    depth = 0
    pos = 0

    for line in data_lines:
        if line.startswith('forward '):
            pos += int(line[8:])
        elif line.startswith('up '):
            depth -= int(line[3:])
        elif line.startswith('down '):
            depth += int(line[5:])

    print(f'Depth : {depth}')
    print(f'Position : {pos}')

    print(depth * pos)
