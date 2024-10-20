items = 1

if items != 2:pass
    #raise Exception("Items are not 2 as expected")

#assert(items == 2)

try:
    with open("textfile.txt",'r') as reader:
        print(reader.read())

except :
    print("File Not FOund")


try:
    with open("textfile.txt",'r') as reader:
        print(reader.read())

except Exception as e:
    print(e)
finally:
    print("Finally block")