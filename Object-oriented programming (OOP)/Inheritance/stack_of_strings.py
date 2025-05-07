

class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        element = reversed(self.data)
        return f"[{', '.join(str(el) for el in element)}]"



s = Stack()
print(s.is_empty())
s.push(6)
s.push(7)
print(s.is_empty())
print(s)
print(s.pop())
print(s)