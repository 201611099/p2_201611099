def charCount(word):
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()

x={'TV','phone','camera','fridger','mixer','audio','cd player','light','computer','notebook','recorder'}
y={'coffee machine','radio','camera','running machine','ramp','computer','notebook','recorder'}

def intersection():
    print x.intersection(y)
    
def myappliances():
    print x.difference(y)
    
def friendappliances():
    print y.difference(x)
    
def union():
    print x.union(y)
    
def appliances():
    intersection()
    myappliances()
    friendappliances()
    union()
    print len(x.union(y))
    
def lab9():
    word='sangmyung university'
    charCount(word)
    appliances()
    
def main():
    lab9()
    
if __name__=="__main__":
    main()