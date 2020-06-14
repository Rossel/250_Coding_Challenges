var = 8
     
def my_func(x):
    global var
    print(x * var)
    var = 12
    	
my_func(10)