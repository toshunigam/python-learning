#Ask a user to input a number between 1 to 10. give the user only 3 chance to enter correct value. if the user enter the correct value then print it other wise give error saying "Sorry your chances are over"
counter = 0
while counter < 4:
    number = int(raw_input("Please enter number between one to ten>>"))
    if number<10:
        print 'Valid number'
        break
    elif number>1:
        print 'valid number'
        break
    else:
        print 'Invalid attempt'
        counter += 1



