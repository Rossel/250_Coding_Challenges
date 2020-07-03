import itertools
     
lam = lambda x: x < 5
     
result = list(itertools.filterfalse(lam, range(10)))
     
print(result)