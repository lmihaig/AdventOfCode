# http://adventofcode.com/2021/day/8

inputFile = open("input.txt").readlines()


def part1():
    ans = 0
    for line in inputFile:
        line = line.split("|")[-1].strip().split()
        for segment in line:
            if len(segment) in [2, 3, 4, 7]:
                ans += 1
    return ans


hmap = {"acedgfb": 8,
        "cdfbe": 5,
        "gcdfa": 2,
        "fbcad": 3,
        "dab": 7,
        "cefabd": 9,
        "cdfgeb": 6,
        "eafb": 4,
        "cagedb": 0,
        "ab": 1}


def part2():
    return None


if __name__ == "__main__":

    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
