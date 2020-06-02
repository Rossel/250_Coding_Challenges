x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
     
if sum(x[0]) > sum(x[2]):
    print("True!")
elif max(x[1]) > max(x[2]):
    print("False!")
else:
    print("None!")