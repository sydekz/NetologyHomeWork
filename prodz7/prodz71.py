

class LIFO:

    def __init__(self):
        self.queue = list()

    def isEmpty(self):
        return True if len(self.queue) == 0 else False

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        return self.queue.pop()

    def peek(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)




