f = open("test.txt", "w")
     
f.write("python")
f.close()
     
f = open("test.txt", "r")
     
print(f.read())