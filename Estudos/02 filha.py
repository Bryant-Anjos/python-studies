class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self, element):
        self.queue.append(element)
        self.len_queue += 1

    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def length(self):
        return self.len_queue

    def front(self):
        if not self.empty():
            return self.queue[0]
        return None


q = Queue()

q.push(1)
q.push(2)
q.push(3)

q.pop()
q.pop()
q.pop()

print(q.front())

print(q.length())
