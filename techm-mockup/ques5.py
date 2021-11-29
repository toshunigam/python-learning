#Enter an email address from the user and check if it is valid of not.[Hint-check for the presence of @ sign]
email = raw_input("Enter your email address:")
ismail = email.find('@')
if ismail>0:
    print 'valid'
else:
    print 'invalid'
