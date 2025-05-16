f = open("user.txt","r+")
print(f.read())
f.write("Japan")
f.close()

#r+ mode reads the file as well as writes in file