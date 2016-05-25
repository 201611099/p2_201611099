def outputNumber():
    data=[1,2,3,4,5,6,7,8,9,10]
    for i in data:
        print "{0}\t".format(i),
        if i%2==0:
            print
            
def lab13():
    outputNumber()
    
def main():
    lab13()

if __name__=="__main__":
    main() 