def fibonacci_generation():
    """
    This function generates numbers of fibonacci
    """
    a, b = 0, 1 
    yield a
    yield b
    
    while True:
        a, b = b, a + b
        yield b
        
        
for i in fibonacci_generation():
    if i > 100:
        break
    print(i, end= ' ')
        