x = [1, 2]
y = [10, 100]
     
for i in x:
    for j in y:
        if i % 2 == 0:
            continue
            print(i * j)
        print(i)
    print(j)