# http://adventofcode.com/2016/day/1

commands = open("input.txt").readline().strip().split(", ")


def part1():
    heading = 0
    x = 0
    y = 0
    for command in commands:
        if command[0] == "R":
            heading = (heading + 1) % 4
        else:
            heading = (heading - 1) % 4

        dist = int(command[1:])

        match heading:
            case 0:
                x += dist
            case 1:
                y += dist
            case 2:
                x -= dist
            case 3:
                y -= dist

    return abs(x) + abs(y)


headings = {0: (0, 1),   # N
            1: (1, 0),   # E
            2: (0, -1),  # S
            3: (-1, 0)   # W
            }


def part2():
    visited = []
    heading = 0
    cur_loc = (0, 0)
    for i, command in enumerate(commands):
        if command[0] == "R":
            heading = (heading + 1) % 4
        else:
            heading = (heading - 1) % 4

        dist = int(command[1:])

        for i in range(dist):
            cur_loc = (cur_loc[0] + headings[heading][0],
                       cur_loc[1] + headings[heading][1])
            if cur_loc in visited:
                return abs(cur_loc[0]) + abs(cur_loc[1])
            visited.append(cur_loc)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
