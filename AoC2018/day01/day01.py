# http://adventofcode.com/2018/day/1

from itertools import accumulate, cycle


input = open("input.txt").readlines()


def part1():
    return sum([int(i) for i in input])


def part2():
    frequencies = [int(i) for i in input]
    seen = {0}
    return next(f for f in accumulate(cycle(frequencies)) if f in seen or seen.add(f))


if __name__ == "__main__":

    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
