from collections import deque
inputFile = open("day18.txt", mode="r")

operators = {   "+": (lambda a, b: a + b),
                "*": (lambda a, b: a * b),
                "(": 0,
                ")": 0
}

nums1 = []
nums2 = []

def toRPN(expr, priority):
    rpn = ""
    stack = deque()

    for char in expr:
        if char.isnumeric():
            rpn += char + " "
        elif char in operators:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    lastChar = stack.pop()
                    while lastChar != "(":
                        rpn += lastChar + " "
                        lastChar = stack.pop()
                else:
                    stackTop = stack[-1]
                    if priority[char] > priority [stackTop]:
                        stack.append(char)
                    else:
                        rpn += stack.pop() + " "
                        stack.append(char)
    while len(stack) > 0:
        rpn += stack.pop() + " "
    return rpn

def calcRPN(rpn):
    stack = deque()
    for char in rpn:
        if char.isnumeric():
            stack.append(char)
        elif char in operators:
            a = int(stack.pop())
            b = int(stack.pop())
            result = operators[char](a, b)
            stack.append(result)
    return stack.pop()

priority1 = {"+": 1, "*": 1, "(": 0, ")": 0}
priority2 = {"+": 2, "*": 1, "(": 0, ")": 0}

for line in inputFile:
    line = line.strip()
    RPN1 = toRPN(line, priority1)
    RPN2 = toRPN(line, priority2)
    nums1.append(calcRPN(RPN1))
    nums2.append(calcRPN(RPN2))

print("Task1:", sum(nums1))
print("Task2:", sum(nums2))