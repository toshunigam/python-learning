#This is a calculator module which is used by ques13.py file
def add(*number):
    total_sum=0
    for i in number:
        total_sum +=i
    print "Total SUM:",total_sum
    return
def subtract(a,b):
    c = a-b
    print c
    return
def multiply(a,b):
    c = a*b
    print c
    return
def divide(a,b):
    c = a/b
    print c
    return

