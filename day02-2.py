import io

if __name__ == '__main__':
    data = io.open('day02_input.txt', 'r').read()
    data_lines = data.split('\n')

    depth = 0
    pos = 0
    aim = 0

    for line in data_lines:
        if line.startswith('forward '):
            pos += int(line[8:])
            depth += int(line[8:]) * aim
        elif line.startswith('up '):
            aim -= int(line[3:])
        elif line.startswith('down '):
            aim += int(line[5:])

    print(f'Depth : {depth}')
    print(f'Position : {pos}')
    print(f'Aim : {aim}')

    print(depth * pos)
