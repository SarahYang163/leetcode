class MinStack:

    def __init__(self):
        self.stack = []
        self.helpStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.helpStack) != 0 and val < self.helpStack[-1]:
            self.helpStack.append(val)
        elif len(self.helpStack) != 0 and val >= self.helpStack[-1]:
            self.helpStack.append(self.helpStack[-1])
        else:
            self.helpStack.append(val)

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop()
            self.helpStack.pop()
        else:
            raise Exception

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) != 0 else None

    def getMin(self) -> int:
        return self.helpStack[-1] if len(self.helpStack) != 0 else None


if __name__ == '__main__':
    stack=[3,2,3]
    stack.remove(stack[len(stack)-1])