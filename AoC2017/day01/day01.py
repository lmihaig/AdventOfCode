# http://adventofcode.com/2017/day/1

input = open("input.txt").readline().strip()


def part1():
    ans = 0
    if input[0] == input[-1]:
        ans += int(input[0])
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            ans += int(input[i])
    return ans


def part2():
    ans = 0
    step = len(input) // 2
    for i in range(len(input)):
        if input[i] == input[(i + step) % len(input)]:
            ans += int(input[i])
    return ans


if __name__ == "__main__":

    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
