# Division by two is a problem where you convert the decimal into binary equivalent

from stack import Stack


def convert_decimal_to_binary(stack, decimal):
    if decimal == 0:
        return 0

    while decimal != 0:
        remainder = str(decimal % 2)
        stack.push(remainder)
        decimal = decimal // 2

    binary = ""
    while not stack.is_empty():
        binary += stack.pop()

    return binary


def main():
    stack = Stack()
    decimal = 1211

    print(convert_decimal_to_binary(stack, decimal))


if __name__ == "__main__":
    main()
