#write a program that ask user for five flower, and then store them in a list called flowerlist and print them out into alphabetical order
counter = 0
flowerlist = []
while(counter<5):
    flowerlist.append(raw_input('Enter flower:'))
    counter = counter + 1

flowerlist.sort()
print(flowerlist)
#for flo in flowerlist.sort():
 #   print flo
