# http://adventofcode.com/2019/day/1
input = open("input.txt").readlines()
input = [int(i) for i in input]


def part1():
    return sum(i // 3 - 2 for i in input)


def part2():
    ans = 0
    nums = input
    for i in range(len(nums)):
        while nums[i]:
            nums[i] = max(0, nums[i] // 3 - 2)
            ans += nums[i]
    return ans


if __name__ == "__main__":

    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
