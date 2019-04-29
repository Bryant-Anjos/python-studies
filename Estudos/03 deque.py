# deque - double-ended queue

class Deque:

    def __init__(self):
        self.deque = []
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, element):
        self.deque.insert(0, element)
        self.len += 1

    def push_back(self, element):
        self.deque.insert(self.len, element)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1

    def pop_back(self):
        if not self.empty():
            self.deque.pop(self.len - 1)
            self.len -= 1

    def front(self):
        if not self.empty():
            return self.deque[0]

    def back(self):
        if not self.empty():
            return self.deque[-1]

    def print_deque(self):
        for i in self.deque:
            print(i, end=' ')


d = Deque()

print(d.empty())

d.push_front(3)
d.push_front(7)
d.push_back(18)
d.push_front(9)
d.push_back(30)

print(d.empty())
d.print_deque()
print('\nFront: %d' % d.front())
print('Back: %d' % d.back())

d.pop_back()
d.pop_back()
d.pop_front()

d.print_deque()
print('\nFront: %d' % d.front())
print('Back: %d' % d.back())