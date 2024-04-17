class FilterIterator:
    def __init__(self, iterable, func):
        self.iterable = iter(iterable)
        self.func = func
 
    def __iter__(self):
        return self
    
    
    def __next__(self):
        while True:
            value = next(self.iterable)
            if self.func(value):
                return value
        
               
f_iter = FilterIterator([1, 2, 3, 4], lambda x: x % 2 == 0)
while True:
    try:
        print(next(f_iter), end=" ")
    except StopIteration:
        break
        