"""
@author LHJ
@since 160406
"""
def Leapyear():
    year=raw_input("year: ")
    year=int(year)
    if (year%4==0) and (year%100!=0 or year%400==0):
        res="It's a Leap year"
    else:
        res="It isn't a Leap year"
    print res
    return res

def lab6()
    Leapyear()

def main():
    lab6()

if __name__=="__main__":
    main()