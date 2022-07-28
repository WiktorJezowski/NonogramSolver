from queue import Queue

class MyQueue:
    def __init__(self, n, m, full=False):
        self.rows_stored = [full] * n
        self.columns_stored = [full] * m
        self.queue = Queue()
        if full:
            for i in range(n):
                self.queue.put(('r', i))
            for i in range(m):
                self.queue.put(('c', i))

    def clear(self):
        while not self.empty():
            self.get()

    def empty(self):
        return self.queue.empty()

    def put(self, x):
        if x[0] == 'r' and not self.rows_stored[x[1]]:
            self.queue.put(x)
            self.rows_stored[x[1]] = True
        elif x[0] == 'c' and not self.columns_stored[x[1]]:
            self.queue.put(x)
            self.columns_stored[x[1]] = True

    def get(self):
        if not self.queue.empty():
            x = self.queue.get()
            if x[0] == 'r':
                self.rows_stored[x[1]] = False
            elif x[0] == 'c':
                self.columns_stored[x[1]] = False
            return x
        return 'e', -1