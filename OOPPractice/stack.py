class Stack:
    def __init__(self) -> None:
        self.stack = []

    def add(self, obj):
        self.stack.append(obj)

    def remove(self):
        self.stack.pop()
    def __repr__(self) -> str:
        if len(self.stack) == 0:
            return "The stack is empty"
        else:
            return f"Stack: {self.stack}"
        
class Queue(Stack):
    def __init__(self) -> None:
        self.stack = []
        self.queue = self.stack
    def remove(self):
        self.queue.pop(0)
    def __repr__(self) -> str:
        if len(self.queue) == 0:
            return "The queue is empty."
        else:
            return f"Queue: {self.queue}"


def main():
    stack = Stack()
    stack.add(45)
    stack.add(78)
    stack.add(93)
    print(stack)
    stack.remove()
    stack.remove()
    print(stack)
    queue = Queue()
    queue.add('Hello')
    queue.add('world')
    queue.add('!')
    print(queue)
    queue.remove()
    queue.remove()
    print(queue)

main()