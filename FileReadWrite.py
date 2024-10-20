path = r"C:\Users\Chirag M. Sidhdhapur\Desktop\New Text Document.txt"
pathNew = path.replace("\\","/")
"""
f = open(pathNew, 'w')
x = f.read()
print(type(x))
print(x)
print("------------------")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline()) 
line = f.readlines()
print(line)
f.close() """

with open(pathNew, 'r') as readfile :
    l = readfile.readlines()

lr = l[::-1]

with open(pathNew, 'w') as writer :
    for item in lr:
        writer.write(item)