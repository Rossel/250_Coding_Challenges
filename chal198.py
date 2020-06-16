f = open("test.txt", "w")
     
f.writelines(['python', ' ', 'and', ' ', 'java'])
f.close()
     
f = open("test.txt", "r")
     
print(f.read())