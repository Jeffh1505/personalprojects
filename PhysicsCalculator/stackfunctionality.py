class Stack:
    def __init__(self) -> None:
        self.stack = []

    def add(self, obj):
        self.stack.append(obj)

    def remove(self):
        self.stack.pop()

    def get_last(self):
        if not self.stack:
            raise IndexError("Stack is empty")  # Accessing the last element in the stack
        else:
            return self.stack[-1]
        
    def __repr__(self) -> str:
        if len(self.stack) == 0:
            return "The stack is empty"
        else:
            return f"Stack: {self.stack}"