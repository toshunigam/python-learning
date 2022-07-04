import datetime
#Input your age into valiable called age. Have the computer printout how old you'll be like eight years from now, ten years from now etc.
d = datetime.datetime.now()
age = input('Enter Your birth year:')
print("You are %s year old" %(d.year-int(age)))
