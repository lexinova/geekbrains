import re
from typing import List


def entry() -> str:
    infix = input("Enter algebraic data: ")
    return infix


def infix_to_list(infix: str) -> List[str]:
    infix = re.sub(re.compile(r'\s+'), '', infix)
    digit = []
    result = []
    for x in infix:
        if x == "." or x.isdigit():
            digit.append(x)
        elif x != '.':
            if len(digit) > 0:
                result.append("".join(digit))
                digit = []
            result.append(x)
    if len(digit) > 0:
        result.append("".join(digit))
    return result


def weight(item):
    if item == "+" or item == "-":
        return 0
    else:
        return 1


def infix_to_postfix_list(infix: str) -> List[str]:
    stack = []
    result = []
    for item in infix_to_list(infix):
        if item in "+-*/":
            while stack and stack[-1] != "(" and weight(item) <= weight(stack[-1]):
                result.append(stack.pop())
            stack.append(item)
        elif item == ")":
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                result.append(x)
        elif item == "(":
            stack.append(item)
        else:
            result.append(float(item))
    while stack:
        result.append(stack.pop())
    return result


def postfix_calculate(postfix_list):
    stack = []
    for item in postfix_list:
        if item == "+" or item == "-" or item == "*" or item == "/":
            x, y = stack.pop(), stack.pop()
            if item == "+":
                stack.append(x + y)
            elif item == "-":
                stack.append(x - y)
            elif item == "*":
                stack.append(x * y)
            else:
                stack.append(x / y)
        else:
            stack.append(item)
    return stack[0]


def output(postfix: str, result: float) -> None:
    print("{}\n{}".format(postfix, result))


def main():
    postfix = infix_to_postfix_list(entry())
    result = postfix_calculate(postfix)
    output(postfix, result)


if __name__ == '__main__':
    main()

