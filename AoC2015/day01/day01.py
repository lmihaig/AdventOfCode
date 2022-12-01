# http://adventofcode.com/2015/day/1

input = open("input.txt").readline().strip()


def part1():
    floor = 0
    for c in input:
        if c == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def part2():
    floor = 0
    ch_index = 0
    for c in input:
        ch_index += 1
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return ch_index


if __name__ == '__main__':
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
