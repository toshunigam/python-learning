first = 'toshu'
last = "nigam"
print(first + last) #there is no difference between single and double quotes in terms of string

#make first letter capital
camelcase = "this is for a camelcase testing"
print(camelcase.upper())
print(camelcase.capitalize())
tmp = camelcase.split(' ')
# print(tmp)
arr = []
i=0
for val in tmp:
    arr.insert(i, val.capitalize())
    i = i + 1
print(' '.join(arr))