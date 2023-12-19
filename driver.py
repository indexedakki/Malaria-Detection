# def superDigit(n, k):
#     n=int(n)
#     if n<10:
#         return n
#     else:
#         n=str(n)*k
#         n=list(n)
#         n=[int(i) for i in n]
#         r=sum(n)
#         value=superDigit(r,1)
        
#     return value

# nk = input().split()

# n = nk[0]

# k = int(nk[1])

# result = superDigit(n, k)
# print(result)

# import itertools
# item=[]
# def combiner(zeros, ones):
#     for indices in itertools.combinations(range(zeros+ones), ones):
#         item = ['0'] * (zeros+ones)
#         for index in indices:
#             item[index] = '1'
#         yield ''.join(item)
# val= (list(combiner(3,1)))
# pass

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



