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

word='sangmyung university'
def lab9():
    charCount(word)
    
def main():
    lab9()
    
if __name__=="__main__":
    main()