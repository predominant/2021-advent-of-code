import io

if __name__ == '__main__':
    data = io.open('day03_input.txt', 'r').read()
    data_lines = data.split('\n')

    buckets = []
    for line in data_lines:
        for i in range(len(line)):
            bit = int(line[i])
            if len(buckets) <= i:
                buckets.append({0: 0, 1: 0})
            buckets[i][bit] += 1

    result = ""
    for bit in buckets:
        if bit[0] > bit[1]:
            result += "0"
        else:
            result += "1"

    print(result)

    gamma = int(result, 2)
    print(f'Gamma : {gamma}')

    flip_bits = result.replace('1', 'x')
    flip_bits = flip_bits.replace('0', '1')
    flip_bits = flip_bits.replace('x', '0')
    epsilon = int(flip_bits, 2)
    print(f'Epsilon : {epsilon}')

    print(gamma * epsilon)