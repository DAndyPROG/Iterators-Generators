class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)
        self.next_value = next(self.iterator)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.next_value
        self.next_value = next(self.iterator, None)
        
        if self.next_value is  None:
            self.iterator = iter(self.iterable)
            self.next_value = next(self.iterator)

        return value
    
    def peak(self):
        
        return self.next_value


cycle_iter = CyclicIterator([1, 2, 3])

for i in range(10):
    print(next(cycle_iter))
    print(cycle_iter.peak())
    print(next(cycle_iter))
