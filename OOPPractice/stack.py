class Stack:
    def __init__(self) -> None:
        self.stack = []

    def add(self, obj):
        self.stack.append(obj)

    def remove(self):
        self.stack.pop()





def main():
    stack = Stack()
    stack.add(45)
    stack.add(78)
    stack.add(93)
    print(stack.stack)
    stack.remove()
    stack.remove()
    print(stack.stack)

main()