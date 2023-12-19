import itertools
item=[]
def combiner(zeros, ones):
    val=[]
    n=list(itertools.combinations(range(zeros+ones),ones))
    p=0
    for i in range(len(n)):
        item=['0' for i in range(zeros+ones)]
        index=n[p]
        for i in index:
            item[i]='1'
        val.append(''.join(item))
        p+=1
    return val
for _ in range(int(input())):
    n,m=map(int,input().split())
    val=list(combiner(n,m))
    cnt=0
    for i in val:
        if i[0]=='1':
            cnt+=1
    print(cnt)



