# validate an IP adress

ip = "10.0.23.432"
# ip address to check for validity
ipArrary = ip.split('.')
print(ipArrary)
isValid=''
for i in range(len(ipArrary)):
    if int(ipArrary[i]) > 256:
        isValid=False
    else :
        isValid=True

print('You have entered ip addres is :',isValid)
    
