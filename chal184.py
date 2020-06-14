def my_func(x, *args):
    return x * args[1]
     
result = my_func(5, 10, 20, 30, 50)
print(result)