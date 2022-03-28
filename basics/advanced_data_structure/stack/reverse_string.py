from stack import Stack

def reverse_string(stack, string_to_reverse):
    for char in string_to_reverse:
        stack.push(char)
    reverse = ""
    while not stack.is_empty():
        reverse += stack.pop()
    return reverse


def main():
    s = Stack()
    string_var = "Hello World"
    print(reverse_string(s, string_var))

if __name__ == "__main__":
    main()