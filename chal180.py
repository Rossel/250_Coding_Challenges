def my_func(x):
    return len(x) * sorted(x.keys())[-1]
     
result = my_func({1: 3, 2: 3, 4: 5, 5: 9, 6: 8, 3: 7, 7: 0})
print(result)