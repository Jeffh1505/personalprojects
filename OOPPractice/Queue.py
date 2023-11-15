class Queue:
    def __init__(self) -> None:
        self.queue = []


    def insert(self,element):
        self.queue.append(element)

    def remove(self):
        if len(self.queue) == 0:
            return print("The queue is empty.")
        return self.queue[:-3]
    def __repr__(self) -> str:
        return f"Queue: {self.queue}"

queue = Queue()
queue.insert(5)
queue.insert(6)

print(queue)

queue.remove()

print(queue)