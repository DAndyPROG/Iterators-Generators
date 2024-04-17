class RangeIterator:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step
     
       
    def __iter__(self):
        return self


    def __next__(self):
        if self.step > 0:
            if self.current >= self.end:
                raise StopIteration
            result = self.current
            self.current += self.step
            return result


for i in RangeIterator(1, 10, 2):
    print(i)
