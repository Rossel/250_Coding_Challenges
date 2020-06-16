with open("test.txt", "w") as f:
    f.write("python")
     
f = open("test.txt", "r")
     
print(f.read())