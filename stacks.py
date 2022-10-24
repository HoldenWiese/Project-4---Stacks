"Implementation of a stack using python list."

class Stack:
    "Stack ADT class"
    def __init__(self, stack=[]):
        "Initialize class variables"
        self.stack = stack
        self.length = len(self.stack)

    def __str__(self):
        "Return a string of stacks contents"
        r_str = ""
        for item in self.stack:
            r_str += item + " "
        if r_str == "":
            r_str = "Stack is empty"
        return r_str

    def size(self):
        "Return length of stack"
        return self.length

    def push(self, item):
        "Add item to stack and increment"
        self.stack.append(item)
        self.length += 1

    def pop(self):
        "Remove item from stack and decrement"
        if self.length == 0:
            raise IndexError("Cannot pop() empty stack")
        self.stack.pop(self.length - 1)
        self.length -= 1

    def top(self):
        "View next item in stack"
        if self.length == 0:
            raise IndexError("Cannot top() empty stack")
        return self.stack[self.length - 1]

    def clear(self):
        "Empty the stack"
        self.stack = []
