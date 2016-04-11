"""
201611099
"""
def sumList(aList):
    x=list()
    for i in range(0,aList):
        if i%4==0 and i%5!=0:
            x.append(i)
    print x
    sum=0
    for i in range(0,len(x)):
        if i%4==0 and i%5!=0:
            sum+=x[i]
    print sum

def lab6(ms):
    aList=1000
    mysum=sumList(aList)  
    print mysum
ms=1000
lab6(ms)

def main():
    lab6()