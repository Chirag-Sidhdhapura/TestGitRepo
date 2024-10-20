from itertools import count

num = int(input("Enter a Number : "))
"""
if num%2 == 0:
    print("Number",num,"Is Even")
else:
    print("Number",num,"Is Odd")

vow = ['a','e','i','o','u']
string = input("Enter a Statement :")
result = []

for i in string:
    if i in vow:
        continue
    else:
        result.append(i)

a= ''.join(result)

l = a.split(" ")
print(''.join(l)) 

sum=0
for i in range(1,num+1):
    sum= sum +i
print(sum)

for i in range(0,11,2):
    print(i) """
count = 1
while(0 < count <= num ):
    if count == 3 :
        count +=1
        continue
    elif count == 9 :
        break
    print(count, end=" ")
    count+=1