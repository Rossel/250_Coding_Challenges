x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
     
if sum(x[0][-3:]) + sum(x[2][-3:]) == sum(x[1][-3:]):
    print("True!")
elif len(x[0]) * 2 < sum(x[2]):
    print("False!")