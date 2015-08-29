
class CounterIterator(object):
    def __init__(self, count):
        self.count = count
        self.start = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.count:
            self.start = self.start + 1
            return self.start
        raise StopIteration
    

class CounterIterable(object):
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return CounterIterator(self.count)


if __name__ == '__main__':
    c = CounterIterable(5)
    for i in c:
        print(i)
        
    x = CounterIterable(2)
    y = CounterIterable(3)
    for i in x:
        for j in y:
            print(i, j)
    
            