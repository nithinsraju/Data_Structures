class stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def reverse_string(Stack, input_str):
    for i in range(len(input_str)):
        Stack.push(input_str[i])

    rev_str = ""
    while not Stack.is_empty():
        rev_str += Stack.pop()
    return rev_str


Stack = stack()

input_str = "hello"

print(reverse_string(Stack, input_str))
