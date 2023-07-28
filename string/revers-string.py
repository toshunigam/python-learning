# reverse the string
# ``````````````````````````````````````````````
# count the string length
# loop from the last to first
# get the value of string from each iteration
# push it into one array
# print the array which contains revers string
#````````````````````````````````````````````````````
a="Toshu Nigam"
#print(len(a))
b=[]
for i in range(len(a)):
 #   print(i, a[len(a)-(i+1)])
    b += a[len(a)-(i+1)]
    
#print(len(b))
#print(b)
c=''
for s in b:
    c += s
print('Input string :', a)
print('Reversed string :', c)
