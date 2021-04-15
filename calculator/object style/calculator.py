import re
from typing import List


class InterfaceCli:

    def __init__(self):
        self._result = None
        self._infix = None
        self._postfix = None

    def entry(self) -> None:
        infix = input("Enter algebraic data: ")
        self._infix = infix

    def output(self) -> None:
        print("{}\n{}".format(self._postfix, self._result))

    @property
    def get_infix(self):
        return self._infix

    def set_postfix(self, postfix: str):
        self._postfix = postfix

    def set_result(self, result: float):
        self._result = result


def weight(item):
    if item == "+" or item == "-":
        return 0
    else:
        return 1


class Calculator:

    def __init__(self, infix_to_list=None, infix=None, infix_list=None):
        self._infix_to_list = infix_to_list
        self._infix = infix
        self._result = None
        self._infix_list = infix_list
        self._postfix_list = None

    @property
    def get_infix_list(self):
        return self._infix_list

    def set_infix(self, _infix: str):
        self._infix = _infix

    def infix_to_list(self):
        infix = re.sub(re.compile(r'\s+'), '', self._infix)
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
        self._infix_list = result

    def infix_to_postfix_list(self):
        stack = []
        result = []
        for item in self._infix_list:
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
        self._postfix_list = result

    def postfix_calculate(self):
        stack = []
        for item in self._postfix_list:
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
        self._result = stack[0]

    @property
    def get_postfix(self):
        return self._postfix_list

    @property
    def get_result(self):
        return self._result


def main():
    interface_cli = InterfaceCli()
    interface_cli.entry()
    calculator = Calculator()
    calculator.set_infix(interface_cli.get_infix)
    calculator.infix_to_list()
    calculator.infix_to_postfix_list()
    calculator.postfix_calculate()
    interface_cli.set_postfix(calculator.get_postfix)
    interface_cli.set_result(calculator.get_result)
    interface_cli.output()


if __name__ == '__main__':
    main()
