with open("day4.txt", 'r') as file:
    lines = file.read()

nums = lines.splitlines()[0]
nums = [int(num)for num in nums.split(",")]
boards = lines.split("\n\n")[1:]
boards = [board.split("\n") for board in boards]
boards = [[[int(element) for element in line.split()]
           for line in lines] for lines in boards]


def bingo(board, calledNums):
    for i in range(len(board)):
        if all(board[i][j] in calledNums for j in range(len(board[0]))):
            return True
        if all(board[j][i] in calledNums for j in range(len(board[0]))):
            return True
    return False


finishedBoard = [False for board in boards]
calledNums = []
winners = []
for num in nums:
    calledNums.append(num)
    for i, board in enumerate(boards):
        if bingo(board, calledNums) and not finishedBoard[i]:
            finishedBoard[i] = True
            winners.append(
                num*sum(n for row in board for n in row if n not in calledNums))

print("Part1: ", winners[0])
print("Part2: ", winners[-1])
