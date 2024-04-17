from itertools import permutations

def permutations_generator(lst):
    for perm in permutations(lst):
        yield list(perm)
    

for i in permutations_generator([1, 2, 3]):
    print(i)
