class Queue:
    def __init__(self):
        self.queue = []


    def insert(self,element):
        self.queue.append(element)

    def remove(self):
        self.queue = self.queue[:-1]
        return self.queue
    def __repr__(self) -> str:
        if len(self.queue) == 0:
            return "The queue is empty."
        else:
            return f"Queue: {self.queue}"

queue = Queue()
queue.insert(5)
queue.insert(6)
queue.insert(7)

print(queue)

queue.remove()

print(queue)

queue.remove()

print(queue)

queue.remove()
print(queue)