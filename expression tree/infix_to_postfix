#ref https://rextester.com/VGJZ53355

class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, val):
        self.items.append(val)
        self.length += 1

    def pop(self):
        if self.empty():
            return None
        self.length -= 1
        return self.items.pop()

    def size(self):
        return self.length

    def peek(self):
        if self.empty():
            return None
        return self.items[0]

    def empty(self):
        return self.length == 0

    def __str__(self):
        return str(self.items)


precedence = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}


def convert(expression):
    print(__convert(expression.split()))


def __convert(tokens):
    postfix = []
    opstack = Stack()

    for token in tokens:
        if token.isidentifier():
            postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            while True:
                temp = opstack.pop()
                if temp is None or temp == '(':
                    break
                elif not temp.isidentifier():
                    postfix.append(temp)

        else:  # must be operator
            if not opstack.empty():
                temp = opstack.peek()

                while not opstack.empty() and precedence[temp] >= precedence[token] and token.isidentifier():
                    postfix.append(opstack.pop())
                    temp = opstack.peek()

            opstack.push(token)

    while not opstack.empty():
        postfix.append(opstack.pop())

    return postfix


convert("A + B")
convert("A + B * C")
convert("A * ( B + C ) + D")
