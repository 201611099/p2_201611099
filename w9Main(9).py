my2dlist=[
    [74425,76326],
    [61164,61636],
    [109688,115744],
    [144796,146776],
    [174996,181676],
    [177841,177434],
    [204630,205980],
    [223373,232245],
    [161055,166130],
    [171576,176735],
    [279169,293772],
    [239450,251066],
    [148690,156510],
    [182997,196992],
    [237792,242641],
    [283869,296762],
    [209344,210282],
    [118965,114441],
    [186503,186856],
    [195734,203014],
    [254381,249472],
    [212654,295354],
    [271654,295354],
    [319197,335045],
    [229829,231671]
]

for i in my2dlist:
    print i[0]
    print i[1]

print len(my2dlist)

Male_sum=0
for i in my2dlist:
    Male_sum=Male_sum+i[0]
print Male_sum

Male_average=Male_sum/len(my2dlist)
print Male_average

Female_sum=0
for i in my2dlist:
    Female_sum=Female_sum+i[1]
print Female_sum

Female_average=Female_sum/len(my2dlist)
print Female_average

for i in my2dlist:
    Seoul=i[0]+i[1]
    print Seoul
    
Seoul=[150751,122800,225432,291572,356672,355275,410610,455618,327185,348311,572941,490516,305200,379989,480433,580631,419626,233406,373359,398748,503853,508008,567008,654242,461500]
print Seoul
Seoul_Gu=['J.n','J','Y.s','S.d','G.j','D.d.m','J.N','S.b','G.b','D.b','N.w','E.p','S.d.m','M.p','Y.c','G.s','G.r','G.c','Y.d.p','D.j','G.a','S.c','G.n','S.p','G.d']
print Seoul_Gu

import matplotlib
import matplotlib.pyplot as plt

plt.bar(range(len(Seoul)),Seoul,align='center')
plt.xticks(range(len(Seoul)),list(Seoul_Gu))
plt.show()