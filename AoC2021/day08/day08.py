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
    ans = 0
    for code, nums in [line.strip().split("|") for line in inputFile]:
        lens = {len(x): set(x) for x in code.split()}
        num = ''
        # lens[2] = 1
        # lens[3] = 3
        # lens[4] = 4
        # lens[7] = 8
        # has len 5 - contains 7 = 3
        #           - contains three from 4 = 5
        #           - else = 2
        # has len 6 - contains 4 = 9
        #           - contains 7 = 0
        #           - else = 6
        for n in map(set, nums.split()):
            print(n)
            match len(n), len(n & lens[3]), len(n & lens[4]):
                case 2, _, _: num += "1"
                case 3, _, _: num += "7"
                case 4, _, _: num += "4"
                case 7, _, _: num += "8"
                case 5, 3, _: num += "3"
                case 5, _, 3: num += "5"
                case 5, _, _: num += "2"
                case 6, _, 4: num += "9"
                case 6, 3, _: num += "0"
                case 6, _, _: num += "6"
        ans += int(num)
    return ans


if __name__ == "__main__":

    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
